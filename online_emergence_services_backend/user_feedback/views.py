
from user_feedback. models import UserFeedback
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from user_feedback.serializer import FeedbackSerializer

# Create your views here.
class UserFeedbackView(APIView):
    def post(self, request, format=None):
       serializer = FeedbackSerializer(data=request.data) 
       if serializer. is_valid():
           serializer.save()
           return Response({'msg: Feedback Successfully created'}, status=status.HTTP_201_CREATED)
       return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST) 

