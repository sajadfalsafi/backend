from rest_framework import generics
from .models import Copyright
from .serializers import CopyrightSerializer
# Create your views here.

class CopyrightView(generics.ListAPIView):
    serializer_class = CopyrightSerializer

    def get_queryset(self):
        return Copyright.objects.filter(is_active=True)