from django.db import models

class Contact(models.Model):
    fullname = models.CharField(max_length=250, blank=True)
    email = models.EmailField(blank=True)
    message = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.fullname} ({self.email})"