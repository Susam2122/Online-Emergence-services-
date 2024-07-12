from django.urls import path
from services.views import UserServicesView

urlpatterns =[
    path('userservice/', UserServicesView.as_view(), name= 'userservice'),
]