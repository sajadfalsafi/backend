from rest_framework import generics
from .models import Logo
from .serializers import LogoSerializer
# Create your views here.

class LogoView(generics.ListAPIView):
    serializer_class = LogoSerializer
    queryset = Logo.objects.all()