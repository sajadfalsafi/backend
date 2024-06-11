# serializers.py
from rest_framework import serializers
from .models import MenuItem

class NavbarSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuItem
        # fields = ('id', 'title', 'url', 'parent', 'order', 'is_active')
        fields = '__all__'