from django.shortcuts import render, get_object_or_404
from .models import Project
from django.core.paginator import Paginator
# Create your views here.

def project_list(request):
    all_projects =  Project.objects.all().order_by('title')
    paginator = Paginator(all_projects,10)
    
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

def project_detail(request,pk):
    project = get_object_or_404(Project, pk=pk)
    data = {"project": project}
    return render(request, "projects/project_detail.html", data )