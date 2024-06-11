from rest_framework import serializers
from .models import Intro

class IntoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intro
        fields = '__all__'