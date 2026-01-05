from django.db import models
from order.models import Order
#from .models import Delivery

# Create your models here.

class Delivery(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    delivered = models.BooleanField(default=False)
    delivered_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f" Buyurtma uchun Yetkazib berish - {self.order.id}"
