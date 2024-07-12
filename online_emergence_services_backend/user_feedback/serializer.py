from dataclasses import field
from rest_framework import serializers
from user_feedback.models import UserFeedback

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFeedback
        field = ['id', 'user','feedback', 'feedRate', 'feedDesc']
        extra_kwargs = {
           'feedback' :{'feedback': True},
           'feedRate' :{'feedRate': True},
           'feedDesc' : {'feedDesc' : True} 

        }

    def create(self, validated_data):
        user = UserFeedback.objects.create(
            feedback = validated_data['feedback'],
            feedRate = validated_data['feedRate'],
            feedDesc = validated_data['feedDesc']
        )  

        UserFeedback. save()
        return UserFeedback

