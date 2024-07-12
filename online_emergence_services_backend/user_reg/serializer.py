# serializers.py
from rest_framework import serializers
from .models import User_reg

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_reg
        fields = ('email', 'password', 'role')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User_reg.objects.create_user(**validated_data)
        return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_reg
        fields = ('id', 'email', 'role')

class UserRegUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_reg
        fields = ('email', 'role')

class UserRegDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_reg
        fields = ('id',)
