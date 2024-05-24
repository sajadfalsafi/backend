from django.urls import path
from .views import FooterView

app_name = 'footer'

urlpatterns = [
    path('', FooterView.as_view(), name='footer section')
]