from dataclasses import field
from rest_framework import serializers
from services.models import UserServices

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserServices
        field = ['id', 'user', 'service', 'servName', 'servType', 'servDesc', 'servPriority', 'uploadfile']
        extra_kwargs = {
           'service': {'required': True},
           'servName': {'required': True},
           'servType': {'required': True},
           'servDesc': {'required': True},
           'servPriority': {'required': True},
           'uploadfile': {'required': False}
        }
    def create(self, validated_data):
        user = UserServices.objects.create(
            service = validated_data['service'],
            servName= validated_data['servName'],
            servType= validated_data['servType'],
            servDesc= validated_data['servDesc'],
            servPriority= validated_data['servPriority'],
            uploadfile= validated_data['uploadfile']
        )

        UserServices. save()
        return UserServices