from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, ProjectAttachment
from feedback.models import Feedback
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import AddNewProjectForm, ProjectAttachmentForm
from django.db.models import Q
from django.http import HttpResponseForbidden

# Create your views here.

@login_required
def project_list(request):
    all_projects =  Project.objects.all().order_by('title')
    paginator = Paginator(all_projects,5)
    
    page_number = request.GET.get('page',1)
    page_number = int(page_number)
    
    if page_number < 1:
        page_number = 1
        
    elif page_number > paginator.num_pages:
        page_number = paginator.num_pages
        
    page = paginator.page(page_number)
    
    data = {
        'all_projects': page.object_list,
        'page': page,
    }
    
    return render(request, "projects/project_list.html", data)
    
    
    # projects = Project.objects.all()
    # return render(request, "projects/project_list.html", {"projects": projects})

@login_required
def project_detail(request,pk):
    project = get_object_or_404(Project, pk=pk)
    project_attachments = ProjectAttachment.objects.filter(project=project).order_by('-uploaded_at')
    feedback = Feedback.objects.filter(project=project).order_by('-created_at')
    data = {"project": project,
            "feedback": feedback, 
            "attachments": project_attachments
        }
    return render(request, "projects/project_detail.html", data )

@login_required
def add_new_project(request):
    if request.method == "POST":
        forms= AddNewProjectForm(request.POST)
        
        if forms.is_valid():
            cd = forms.cleaned_data
            
            exists = Project.objects.filter(
                created_by=request.user,
                title = cd["title"],
                description= cd["description"].strip(),
                budget = cd["budget"],
                status = cd["status"],
                location = cd["location"],                
            ).exists()
            
            if exists:
                return redirect ("project_list")
            
            add_project = forms.save(commit=False)
            add_project.created_by = request.user
            add_project.save()
            return redirect("project_detail", pk=add_project.pk)
    else:
        forms = AddNewProjectForm()
        
    data= {
        'forms':forms,
        'title':Project.title,
        'description': Project.description,
        'budget': Project.budget,
        'status': Project.STATUS_CHOICES,
        'location': Project.location,
        
    }
    return render(request, "projects/add_project.html", data)

@login_required
def add_project_attachment(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if request.method == "POST":
        form = ProjectAttachmentForm(request.POST, request.FILES)
        if form.is_valid():
            att = form.save(commit=False)
            att.project = project
            att.uploaded_by = request.user
            att.save()
            return redirect("project_detail", pk=project.pk)
    else:
        form = ProjectAttachmentForm()
        
    data = {
        "form": form,
        "project": project,
        
    }

    return render(request, "projects/add_attachment.html", data)

@login_required
def view_projects(request):
    q = request.GET.get("q", "").strip()

    projects = Project.objects.all().order_by("-created_at")

    if q:
        projects = projects.filter(
            Q(title__icontains=q) |
            Q(description__icontains=q) |
            Q(location__icontains=q)
        ).order_by("-created_at")

    context = {
        "q": q,
        "projects": projects,
        "count": projects.count(),
    }
    return render(request, "projects/view_details.html", context)


def is_owner_or_admin(user, project):
    return user.is_superuser or getattr(user, "role", "") == "admin" or project.created_by == user

@login_required
def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if not is_owner_or_admin(request.user, project):
        return HttpResponseForbidden("You do not have permission to edit this project.")

    if request.method == "POST":
        form = AddNewProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect("project_detail", pk=project.pk)
    else:
        form = AddNewProjectForm(instance=project)

    data = {
        "form": form,
        "project": project,
    }
    return render(request, "projects/edit_project.html", data)

@login_required
def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if not is_owner_or_admin(request.user, project):
        return HttpResponseForbidden("You do not have permission to delete this project.")

    if request.method == "POST":
        project.delete()
        return redirect("project_list")

    data = {
        "project": project,
    }
    return render(request, "projects/delete_project.html", data)

