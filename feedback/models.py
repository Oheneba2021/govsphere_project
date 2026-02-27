from django.db import models
from django.conf import settings
from projects.models import Project

# Create your models here.
class Feedback(models.Model):
    PRIORITY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent'),
    )
    
    FEEDBACK_TYPE_CHOICES = (
        ('complaint', 'Complaint'),
        ('suggestion', 'Suggestion'),
        ('question', 'Question'),
        ('appreciation', 'Appreciation'),
        ('issue_report', 'Issue Report')
    )
    
    STATUS_CHOICES = (
        ('submitted', 'Submitted'),
        ('under_review', 'Under Review'),
        ('resolved','Resolved'),
        ('rejected', 'Rejected')
    )
    
    RATING =(
        ('1', 'Poor'),
        ('2', 'Good'),
        ('3', 'Average'),
        ('4', 'Very Good'),
        ('5', 'Excellent')
    )
    
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    priority = models.CharField(max_length=20, choices= PRIORITY_CHOICES, default='low')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    feedback_type = models.CharField(max_length=20, choices= FEEDBACK_TYPE_CHOICES, default='compliant')
    status= models.CharField(max_length=20, choices= STATUS_CHOICES, default= 'submitted')
    admin_reponse = models.TextField(blank=True)
    project_rating= models.CharField(max_length=30, choices=RATING , default='3')
    contractor_rating = models.CharField(max_length=30, choices= RATING, default='3')
    responded_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_anonymous = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    'project',
                    'user',
                    'feedback_type',
                    'message',
                    'is_anonymous',
                    'project_rating',
                    'contractor_rating',
                    'status',
                    
                ],
                name='unique_same_feedback_payload'
            )
        ]
        
    
    def __str__(self):
        return f"Feedback(id={self.id}, project={self.project.title}, user={self.user.username})"