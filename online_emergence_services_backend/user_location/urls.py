from django.urls import path
from user_location.views import UserLocationView

urlpatterns =[
    path('userlocation/', UserLocationView.as_view(),name= 'userlocation'),
] 




