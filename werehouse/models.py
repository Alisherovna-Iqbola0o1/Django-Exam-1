from django.db import models
from seller.models import Seller
# Create your models here.


class Werehouse(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


