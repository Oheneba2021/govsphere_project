from .models import Feedback
from  django import forms
from projects.models import Project

class FeedbackWithProjectForm(forms.ModelForm):
    '''
    User can select the project they want to give feedback on
    '''
    project = forms.ModelChoiceField(
        queryset=Project.objects.all(),
        empty_label="Select a Project",
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = Feedback
        fields = ['project', 'feedback_type', 'priority', 'message', 'is_anonymous', 'project_rating', 'contractor_rating']
        widgets = {
            "message": forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Enter your feedback here...'}),
        }
        
class FeedbackForProjectForm(forms.ModelForm):
    '''Used When project is already Known(from project detail page)'''
    
    class Meta:
        model = Feedback
        fields = ['feedback_type', 'priority', 'message', 'is_anonymous', 'project_rating', 'contractor_rating']
        widgets = {
            "message": forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Enter your feedback here...'}),
        }
        
    