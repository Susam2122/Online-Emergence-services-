from assign_services.models import AssignServices
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from assign_services.serializer import AssignSerializer 


# Create your views here.
class AssignServicesView(APIView):
    def post(self, request, format=None):
        serializer = AssignSerializer(data=request.data)
        if serializer. is_valid():
             serializer.save()
             return Response ({'msg':'AssignServices Successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     
