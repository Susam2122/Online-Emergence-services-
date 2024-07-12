from user_location.models import UserLocation
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from user_location.serializer import LocationSerializer


# Create your views here.
# class UserLocationView(APIView):
#     def post(self, request, format = None ):
#         serializer= LocationSerializer(data= request.data)
#         serializer. is_valid(raise_exception= True)
#         UserLocation= serializer. save()
#         token= get_tokens_for_UserLocation(UserLocation)
#         return Response({'token':token,'msg': 'Location Successfully'},status= status.HTTP_201_CREATED)


class UserLocationView(APIView):
    def post(self, request, format=None):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Location Successfully Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
