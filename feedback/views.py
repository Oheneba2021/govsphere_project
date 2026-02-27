from email.mime import message
from genericpath import exists

from django.shortcuts import render, get_object_or_404, redirect
from .models import Feedback, Project
from .forms import FeedbackWithProjectForm, FeedbackForProjectForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def feedback_list(request):
    all_feedback = Feedback.objects.all()
    paginator = Paginator(all_feedback, 5)
    
    page_number = request.GET.get('page', 1)
    page_number = int(page_number)
    
    if page_number < 1:
        page_number = 1
    
    elif page_number > paginator.num_pages:
        page_number = paginator.num_pages
        
    page = paginator.page(page_number)
    
    data = {
        'feedback_list': page.object_list,
        'page': page,
    }
    return render(request, 'feedback/feedback_list.html', data)

@login_required
def feedback_detail(request,pk):
    feedback = get_object_or_404(Feedback, pk = pk)
    data = {'feedback_detail' : feedback}
    return render (request, "feedback/feedback_detail.html", data)


@login_required
def add_feedback_for_project(request, project_id):
    '''Entry Point #1 Add feedback from a specific project's detail page'''
    project = get_object_or_404(Project, pk = project_id)
    
    if request.method == "POST":
        form = FeedbackForProjectForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit = False)
            feedback.project = project
            feedback.user = request.user
            feedback.save()
            return redirect('project_detail', pk = project_id)
        
        else: 
            form = FeedbackForProjectForm()  
            
        return render(request, "feedback/add_feedback_for_project.html", {'form': form, 'project': project})
    
@login_required
def add_feedback_global(request):
    q = request.GET.get("q", "").strip()

    project_qs = Project.objects.all()
    if q:
        project_qs = project_qs.filter(Q(title__icontains=q) | Q(description__icontains=q))

    if request.method == "POST":
        form = FeedbackWithProjectForm(request.POST)
        # keep dropdown consistent if user searched
        form.fields["project"].queryset = project_qs.order_by("title")

        if form.is_valid():
            cd = form.cleaned_data  # cleaned_data is safe & reliable

            exists = Feedback.objects.filter(
                user=request.user,
                project=cd["project"],
                message=cd["message"].strip(),
                feedback_type=cd["feedback_type"],
                priority=cd["priority"],
                project_rating=cd.get("project_rating"),
                contractor_rating=cd.get("contractor_rating"),
                is_anonymous=cd.get("is_anonymous", False),
            ).exists()

            if exists:
                # Best UX: send them back to the project page (or feedback list)
                return redirect("project_detail", pk=cd["project"].pk)

            feedback = form.save(commit=False)
            feedback.user = request.user
            # status stays default='submitted' in model
            feedback.save()
            return redirect("feedback_detail", pk=feedback.pk)

    else:
        form = FeedbackWithProjectForm()
        form.fields["project"].queryset = project_qs.order_by("title")

    data = {
        "form": form,
        "q": q,
        "project_count": project_qs.count(),
        "projects": project_qs.order_by("title"),

        # only needed if you're manually building selects (but you're using form too)
        "feedback_type_choices": Feedback.FEEDBACK_TYPE_CHOICES,
        "priority_choices": Feedback.PRIORITY_CHOICES,
        "rating_choices": Feedback.RATING,
        "project_rating": Feedback.RATING,
        "contractor_rating": Feedback.RATING,
    }

    return render(request, "feedback/add_feedback_global.html", data)

def is_owner_or_admin(user, feedback):
    return user.is_superuser or getattr(feedback, "user", "") == "admin" or feedback.user == user


@login_required
def edit_feedback(request, pk):
    feedback = get_object_or_404(Feedback, pk=pk)

    if not is_owner_or_admin(request.user, feedback):
        return redirect("feedback_detail", pk=pk)

    if request.method == "POST":
        form = FeedbackWithProjectForm(request.POST, instance=feedback)
        if form.is_valid():
            form.save()
            return redirect("feedback_detail", pk=pk)
    else:
        form = FeedbackWithProjectForm(instance=feedback)

    data = {
        "form": form,
        "feedback": feedback,
        "projects": Project.objects.all(),   # or filter by user/ownership
        "feedback_type_choices": Feedback.FEEDBACK_TYPE_CHOICES,
        "priority_choices": Feedback.PRIORITY_CHOICES,
        "rating_choices": Feedback.RATING,
    }
    return render(request, "feedback/edit_feedback.html", data)

@login_required
def delete_feedback(request, pk):
    feedback = get_object_or_404(Feedback, pk=pk)

    if not is_owner_or_admin(request.user, feedback):
        return redirect("feedback_detail", pk=pk)

    if request.method == "POST":
        feedback.delete()
        return redirect("feedback")

    data = {"feedback": feedback}
    return render(request, "feedback/confirm_delete.html", data)