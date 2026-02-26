from django import forms
from .models import Project, ProjectAttachment


class AddNewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'title',
            'description',
            'budget',
            'status',
            'location',
        ]
        
class ProjectAttachmentForm(forms.ModelForm):
    class Meta:
        model = ProjectAttachment
        fields = ["file_type", "file", "caption"]