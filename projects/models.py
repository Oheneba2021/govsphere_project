from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError


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
        return f"{self.title}"
    

def validate_file_size(f):
    max_mb = 10
    if f.size > max_mb * 1024 * 1024:
        raise ValidationError(f"File too large. Max size is {max_mb}MB.")
    
class ProjectAttachment(models.Model):
    FILE_TYPE_CHOICES = (
        ("image", "Image"),
        ("pdf", "PDF"),
        ("docx", "DOCX"),
    )
    
    project = models.ForeignKey("projects.Project", on_delete=models.CASCADE, related_name = "attachments")
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    
    file_type = models.CharField(max_length=10, choices=FILE_TYPE_CHOICES)
    file = models.FileField(
        upload_to="project_attachments",
        validators=[
            FileExtensionValidator(allowed_extensions=["pdf", "docx", "jpg","jpeg", "png", "webp"]),
            validate_file_size,
        ],
    )
    
    caption = models.CharField(max_length=255, blank=True)
    uploaded_at= models.DateTimeField(auto_now_add=True)
    
    def clean(self):
        if not self:
            return 
        ext = self.file.name.split(".")[-1].lower()
        
        if self.file_type =="pdf" and ext != "pdf":
            raise ValidationError("Uploaded file is not a pdf.\n Make sure your file has a .pdf extension")
        
        if self.file_type == "docx" and ext != "docx":
            raise ValidationError("Uplaoded file is not a document.\n Make sure your file has a .docx extension  ")
    
        if self.file_type == "image" and ext not in ["jpg", "jpeg", "png", "webp"]:
            raise ValidationError("Uploaded file is not an image. \n Make sure your file has the correct image extension ")
        
    def __str__(self):
        return f"{self.project.title} - {self.file_type}"