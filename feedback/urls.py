from django.urls import path
from . import views

urlpatterns = [
    path("", views.feedback_list, name="feedback"),
    path("<int:pk>/", views.feedback_detail, name = "feedback_detail")
]