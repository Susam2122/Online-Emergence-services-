# views.py
from rest_framework import status
from rest_framework.views import APIView
from .serializer import RegisterSerializer, UserLoginSerializer, UserListSerializer, UserRegUpdateSerializer, UserRegDeleteSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .renderers import UserRenderer
from django.contrib.auth import authenticate
from .models import User_reg
from rest_framework import generics
from rest_framework.response import Response

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }

class UserRegView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({'token': token, 'msg': 'Registration Successful'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogin(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({'token': str(refresh.access_token), 'role': user.role, 'msg': 'Login successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'errors': {'non_field_error': ['Email or password is not valid']}}, status=status.HTTP_401_UNAUTHORIZED)

class UserListView(APIView):
    def get(self, request, format=None):
        users = User_reg.objects.all()
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserUpdate(generics.UpdateAPIView):
    queryset = User_reg.objects.all()
    serializer_class = UserRegUpdateSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

class UserRegDeleteView(APIView):
    def delete(self, request, pk, format=None):
        try:
            user = User_reg.objects.get(pk=pk)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except User_reg.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
