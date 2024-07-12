from dataclasses import fields
from rest_framework import serializers
from user_location.models import UserLocation


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLocation
        fields = ['id', 'user','longitude', 'langitude', 'timestamp']
        extra_kwargs ={
          'longitude' : {'required': True}, 
          'latitude' : {'required': True},
          'timestamp' : {'required': True}
        }

    def create(self, validated_data): 
        user = UserLocation.objects.create(
            longitude= validated_data['longitude'],
            latitude= validated_data['latitude'],
            timestamp=validated_data['timestamp']

        )

        UserLocation. save()
        return UserLocation

