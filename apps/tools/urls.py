from django.urls import path
from .views import ListTools, DetailTools

app_name = 'tools'

urlpatterns = [
    path('<int:pk>/', DetailTools.as_view(), name = 'tools_detail'),
    path('', ListTools.as_view(), name='tools_list'),
]