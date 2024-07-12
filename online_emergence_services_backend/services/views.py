
from services.models  import UserServices
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from services.serializer import ServiceSerializer


# Create your views here.
class UserServicesView(APIView):
    def post(self, request, format=None):
        serializer = ServiceSerializer(data=request.data)
        if serializer. is_valid():
            serializer.save()
            return Response({'msg':'Service Successfully reached'}, status=status.HTTP_201_CREATED )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
