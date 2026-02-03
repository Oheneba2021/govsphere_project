from django.db import models
from django.conf import settings
from projects.models import Project

# Create your models here.
class Feedback(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Feedback(id={self.id}, project={self.project.title}, user={self.user.username})"