from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_list, name = "project_list"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
    path("add/", views.add_new_project, name="add_new_project"),
    path("<int:pk>/attachments/add/", views.add_project_attachment, name="add_project_attachment"),
    path("view_project_details", views.view_projects, name="view_project_details"),
    path("<int:pk>/delete/", views.delete_project, name="delete_project"),
    path("<int:pk>/edit/", views.edit_project, name="edit_project"),
]