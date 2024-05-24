from rest_framework import serializers
from .models import FooterLink

class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterLink
        fields = ('id', 'footer', 'text', 'url')