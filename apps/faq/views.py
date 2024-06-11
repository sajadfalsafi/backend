from rest_framework import generics
from .models import FAQ
from .serializers import FaqSerializer
# Create your views here.

class FaqView(generics.ListAPIView):
    serializer_class = FaqSerializer
    queryset = FAQ.objects.all()