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
    paginator = Paginator(all_feedback, 10)
    
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
    '''Entry Point # 2, Global add feedback page : user can select the project they want to give feedback on'''
    
    q = request.GET.get('q', "").strip()
    
    project_qs = Project.objects.all()
    
    if q: 
        project_qs = project_qs.filter(
            Q(title__icontains=q) | Q(description__icontains=q)
        )

    if request.method == "POST":
        form =  FeedbackWithProjectForm(request.POST)
        
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            return redirect("feedback_detail", pk = feedback.project.id)   
        
    else:
        form = FeedbackWithProjectForm()
        form.fields["project"].queryset = project_qs.order_by("title")
        
    return render(
        request,
        "feedback/add_feedback_global.html",
        {
            "form": form,
            'q': q,
            "project_count": project_qs.count(),
            "projects": project_qs.order_by("title"),
            "q": q
        }
    )