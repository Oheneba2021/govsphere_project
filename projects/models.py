from django.db import models
from django.conf import settings


# Create your models here.
class Project(models.Model):
    STATUS_CHOICES = (
        ('proposed', 'Pending Approval'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    )
    
    title = models.CharField(max_length=300)
    description = models.TextField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='proposed')
    location = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Project(id={self.id}, title={self.title}, status={self.status})"