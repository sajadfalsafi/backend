from django.urls import path
from .views import CancerDataView

urlpatterns = [
    path('predict/', CancerDataView.as_view(), name='predict'),
]