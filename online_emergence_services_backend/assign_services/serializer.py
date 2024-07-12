from rest_framework import serializers
from assign_services.models import AssignServices

class AssignSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignServices
        fields = ['id', 'user', 'services', 'assignServ', 'assignDuty', 'assignStatus']
        extra_kwargs = {
            'assignServ': {'required': True},
            'assignDuty': {'required': True},
            'assignStatus': {'required': True}
        }

        
    def create(self, validate_data):
        user = AssignServices.object.create(
            assignServ = validate_data['assignServ'],
            assignDuty = validate_data['assignDuty'],
            assignStatus = validate_data['assignStatus']
        )

        AssignServices.save()
        return AssignServices
