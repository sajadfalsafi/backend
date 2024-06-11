from rest_framework import generics
from .models import Steps
from .serializers import StepsSerializer
# Create your views here.

class StepsView(generics.ListAPIView):
    serializer_class = StepsSerializer
    queryset = Steps.objects.all()