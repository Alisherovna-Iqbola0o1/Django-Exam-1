from django.db import models
from client.models import Client
from werehouse.models import Werehouse
# Create your models here.

class Order(models.Model):
    class Payment_type(models.TextChoices):
        CASH = "cash",
        CART = "cart",
        MERCHANT = "merchant"

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    warehouses = models.ManyToManyField(Werehouse)
    total_price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50) 
    payment_type = models.TextField(
        max_length=3,
        choices = Payment_type.choices,
        default = Payment_type.MERCHANT
    )

    def __str__(self):
        return f"Buyutrma - {self.id}"
