from django.db import models
from user_reg.models import User_reg
from services.models import UserServices

# Create your models here.
class UserFeedback(models.Model):
    user = models.ForeignKey(User_reg, on_delete= models.CASCADE, related_name='feedback')
    service = models.ForeignKey(UserServices, on_delete= models.CASCADE, related_name='feedback')
    feedback = models.CharField(max_length=40)
    feedRate = models.CharField(max_length=40)
    feedDesc = models.CharField(max_length=40)


    def __str__(self): 
        return f"{self.user.firstName} {self.user.lastName} -{self.feedback}, {self.feedRate}, {self.feedDesc}"






