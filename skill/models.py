from django.db import models
from cloudinary.models import CloudinaryField

class Skill(models.Model):
    """ Model for showcasing skills in  portfolio """
    CATEGORY_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('database', 'Database'),
        ('tools', 'Tools & DevOps'),
        ('other', 'Other'),
    ]
    
    PROFICIENCY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    proficiency = models.CharField(max_length=20, choices=PROFICIENCY_CHOICES, default='intermediate')
    icon = CloudinaryField('icon', blank=True, null=True)
    
    featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', 'category', 'name']
    
    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"
