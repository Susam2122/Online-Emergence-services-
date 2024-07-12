from django.db import models
from user_reg.models import User_reg
from services.models import UserServices

# Create your models here.
class AssignServices(models.Model):
    user = models.ForeignKey(User_reg, on_delete=models.CASCADE, related_name='assignservices')
    services = models.ForeignKey(UserServices, on_delete=models.CASCADE, related_name='assignservices')
    assignServ = models.CharField(max_length=40)
    assignDuty = models.CharField(max_length=40)
    assignStatus = models.CharField(max_length=40)


    def __str__(self):
        return f"{self.user.firstName} {self.user.lastName} {self.UserServices.servType} -{self.assignServ}, {self.assignDuty}, {self.assignStatus}"


