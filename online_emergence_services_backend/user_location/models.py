from django.db import models
from user_reg.models import User_reg

# Create your models here.

class UserLocation(models.Model):
    user = models.ForeignKey(User_reg, on_delete= models.CASCADE, related_name='location'  )
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    timestamp = models.DateTimeField(auto_now_add= True)


    def __str__(self):
        return f"{self.user.firstName} {self.user.lastName} -{self.longitude}, {self.latitude} at {self.timestamp}"