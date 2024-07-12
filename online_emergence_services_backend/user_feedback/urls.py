from django.urls import path
from user_feedback.views import UserFeedbackView

urlpatterns =[
    path('userfeedback/', UserFeedbackView.as_view(), name= 'userfeedback'),
] 