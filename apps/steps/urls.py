from django.urls import path
from .views import StepsView

app_name = 'steps'

urlpatterns = [
    path('', StepsView.as_view(), name='steps section')
]