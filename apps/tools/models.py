from django.db import models

# Create your models here.

class Tools(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(blank=True, upload_to='img/tools/')
    files = models.FileField(blank=True)
    scripts = models.TextField(blank=True)
    eternal_link = models.URLField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    