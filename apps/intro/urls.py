from django.urls import path
from .views import IntroView

app_name = 'intro'

urlpatterns = [
    path('', IntroView.as_view(), name='intro section')
]