# views.py
from rest_framework import generics
from .models import CopyRight, Social
from .serializers import CopyRightSerializer, SocialSerializer

class CopyRightListCreate(generics.ListCreateAPIView):
    queryset = CopyRight.objects.all()
    serializer_class = CopyRightSerializer

class CopyRightDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CopyRight.objects.all()
    serializer_class = CopyRightSerializer

class SocialListCreate(generics.ListCreateAPIView):
    queryset = Social.objects.all()
    serializer_class = SocialSerializer

class SocialDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Social.objects.all()
    serializer_class = SocialSerializer
