from django.db import models

# Create your models here.

class Logo(models.Model):
    title = models.CharField(max_length=250, blank=True)
    subtitle = models.CharField(max_length=250, blank=True)
    image = models.ImageField(upload_to='media/img/logo/', null=True, blank=True)

    def __str__(self):
        return self.title
    