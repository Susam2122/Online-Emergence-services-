from django.urls import path
from assign_services.views import AssignServicesView

urlpatterns =[
    path('assignservices/', AssignServicesView.as_view(), name= 'assignservices')
]