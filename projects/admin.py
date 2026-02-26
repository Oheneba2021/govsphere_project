from django.contrib import admin
from .models import Project, ProjectAttachment
# Register your models here.

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "budget","location", "status","description", "created_at","show_creator",)
    list_filter = ("created_at", "status",)
    search_fields = ("title", "location")

    def show_creator(self, obj):
        if obj.created_by is None:
            return "Unknown"
        return f"{obj.created_by.username}"
    show_creator.short_description = "Created By"
admin.site.register(Project, ProjectAdmin)

class ProjectAttachmentAdmin(admin.ModelAdmin):
    list_display = ("id", "project", "file", "uploaded_at")
    list_filter = ("uploaded_at",)
    search_fields = ("project__title",)
admin.site.register(ProjectAttachment, ProjectAttachmentAdmin)