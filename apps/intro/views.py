from rest_framework import generics
from .models import Intro
from .serializers import IntoSerializer
# Create your views here.

class IntroView(generics.ListAPIView):
    serializer_class = IntoSerializer
    queryset = Intro.objects.all()