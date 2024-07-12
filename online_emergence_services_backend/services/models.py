from django.db import models
from user_reg.models import User_reg

# Create your models here.
class UserServices(models.Model):
    user = models.ForeignKey(User_reg, on_delete= models.CASCADE, related_name='services')
    service = models.CharField(max_length=50) 
    servName = models.CharField(max_length=50)
    servType = models.CharField(max_length=50)
    servDesc = models.CharField(max_length=50)
    servPriority = models.CharField(max_length=50)
    uploadfile = models.ImageField(upload_to='image/')

    def __str__(self):
        return f"{self.user.firstName} {self.user.lastName} -{self.service}, {self.servName}, {self.servType}, {self.servDesc}, {self.servPriority}, {self.uploadfile}" 



