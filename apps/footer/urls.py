# from django.urls import path
# from .views import FooterView

# app_name = 'footer'

# urlpatterns = [
#     path('', FooterView.as_view(), name='footer section')
# ]

# urls.py
from django.urls import path
from .views import CopyRightListCreate, CopyRightDetail, SocialListCreate, SocialDetail

urlpatterns = [
    path('copyrights/', CopyRightListCreate.as_view(), name='copyright-list-create'),
    path('copyrights/<int:pk>/', CopyRightDetail.as_view(), name='copyright-detail'),
    path('socials/', SocialListCreate.as_view(), name='social-list-create'),
    path('socials/<int:pk>/', SocialDetail.as_view(), name='social-detail'),
]