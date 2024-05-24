from rest_framework import generics
from .models import FooterLink
from .serializers import FooterSerializer
# Create your views here.

class FooterView(generics.ListAPIView):
    serializer_class = FooterSerializer
    queryset = FooterLink.objects.all()

    # def get_queryset(self):
    #     return FooterLink.objects.filter(is_active=True)