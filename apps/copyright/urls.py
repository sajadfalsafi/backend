from django.urls import path
from .views import CopyrightView

app_name = 'copyright'

urlpatterns = [
    path('', CopyrightView.as_view(), name='copyright section')
]