from django.urls import path
from user_reg.views import UserRegView,UserLogin, UserListView,UserUpdate, UserRegDeleteView

urlpatterns =[
    path('userregister/', UserRegView.as_view(),name='userregister'),
    path('login/', UserLogin.as_view(),name='login'),
    path('list/',UserListView.as_view(),name='list'),
    path('update/<int:pk>/',UserUpdate.as_view(), name='update_User_reg'),
    path('delete/<int:pk>/',UserRegDeleteView.as_view(), name='delete')
]