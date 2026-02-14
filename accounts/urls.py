from django.urls import path
from .models import views

# 
urlspatterns=[
    path("", views.loginView, name = "login" )
]