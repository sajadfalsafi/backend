from django.urls import path
# from .views import ContactButtonView
from .views import contact_form

app_name = 'contact'

urlpatterns = [
    path('', contact_form, name='contact section')
]