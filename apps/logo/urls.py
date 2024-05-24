from django.urls import path
from .views import LogoView

app_name = 'logo'

urlpatterns = [
    path('', LogoView.as_view(), name='logo section')
]