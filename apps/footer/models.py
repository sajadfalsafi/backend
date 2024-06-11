from django.db import models

# Create your models here.
class CopyRight(models.Model):
    copyright = models.CharField(max_length=250)

    def __str__(self):
        return self.copyright

class Social(models.Model):
    title = models.CharField(max_length=250)
    url = models.CharField(max_length=100)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title
    
# class Footer(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField(blank=True, null=True)
#     is_active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title

# class FooterLink(models.Model):
#     footer = models.ForeignKey(Footer, on_delete=models.CASCADE, related_name='links')
#     text = models.CharField(max_length=100)
#     url = models.URLField()

#     def __str__(self):
#         return self.text
