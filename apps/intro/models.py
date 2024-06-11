from django.db import models

# Create your models here.

class Intro(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    image = models.ImageField(blank=True, upload_to='media/img/intro/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    