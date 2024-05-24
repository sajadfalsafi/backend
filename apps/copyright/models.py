from django.db import models

# Create your models here.

class Copyright(models.Model):
    text = models.CharField(max_length=200)
    year_range = models.CharField(max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text