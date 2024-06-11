# serializers.py
from rest_framework import serializers
from .models import CopyRight, Social

class CopyRightSerializer(serializers.ModelSerializer):
    class Meta:
        model = CopyRight
        fields = '__all__'

class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = '__all__'