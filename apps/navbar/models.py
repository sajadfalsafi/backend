# models.py
from django.db import models
from apps.tools.models import Tools

class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=250, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    tool = models.ForeignKey(Tools, null=True, blank=True, on_delete=models.SET_NULL, related_name='menu_items')
    
    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title