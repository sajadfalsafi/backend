# views.py
from rest_framework import generics
from .models import Tools
from .serializers import ToolsSerializer
# Create your views here.

# class ToolsView(generics.ListAPIView):
#     serializer_class = ToolsSerializer

#     def get_queryset(self):
#         return Tools.objects.filter(is_active=True)
class ListTools(generics.ListAPIView):
    serializer_class = ToolsSerializer

    def get_queryset(self):
        return Tools.objects.filter(is_active=True)


class DetailTools(generics.RetrieveAPIView):
    serializer_class = ToolsSerializer

    def get_queryset(self):
        return Tools.objects.filter(is_active=True)