from django.contrib import admin
from .models import Feedback
# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("id",  "show_user", "show_project", "message", "created_at",)
    list_filter = ("created_at",)
    search_fields = ("show_project", "message")
    
    def show_user(self, obj):
        if obj.user is None:
            return "Anonymous"
        return f"{obj.user.username} "
    show_user.short_description = "User"
    
    def show_project(self, obj):
        if obj.project is None:
            return "No Project"
        return f"{obj.project.title} "
    show_project.short_description = "Project"

admin.site.register(Feedback, FeedbackAdmin)