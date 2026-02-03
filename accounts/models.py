from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = (
        ('citizen', 'Citizen'),
        ('official', 'Official'),
        ('admin', 'Admin'),
        
    )

    role = models.CharField(max_length = 20, choices = ROLE_CHOICES, default= 'citizen')
    
    def __str__(self):
        return f"User(id={self.id}, username={self.username}, role={self.role})"    
# Create your models here.
