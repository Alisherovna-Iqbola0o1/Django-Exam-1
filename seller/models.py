from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience = models.PositiveIntegerField()  
    salary = models.PositiveIntegerField()     

    def __str__(self):
        return self.user.username
