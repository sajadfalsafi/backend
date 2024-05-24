# from rest_framework import generics
# from .models import ContactButton
# from .serializers import ContactButtonSerializer

# # Create your views here.

# class ContactButtonView(generics.ListAPIView):
#     serializer_class = ContactButtonSerializer

#     def get_queryset(self):
#         return ContactButton.objects.filter(is_active=True)



from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from .models import Item
# from .serializers import ItemSerializer
from .serializers import ContactButtonSerializer

@api_view(['POST'])
def contact_form(request):
    if request.method == 'POST':
        serializer = ContactButtonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
