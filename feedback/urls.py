from django.urls import path
from . import views

urlpatterns = [
    path("", views.feedback_list, name="feedback"),
    path("<int:pk>/", views.feedback_detail, name = "feedback_detail"),
    path("projects/<int:project_id>/add/", views.add_feedback_for_project, name = "add_feedback_for_project"),
    path("feedback/add/", views.add_feedback_global, name = "add_feedback_global"),
]