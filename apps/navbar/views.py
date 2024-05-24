# views.py
from rest_framework import generics
from .models import MenuItem
from .serializers import NavbarSerializer
# Create your views here.

class NavbarView(generics.ListAPIView):
    serializer_class = NavbarSerializer

    def get_queryset(self):
        return MenuItem.objects.filter(is_active=True)
