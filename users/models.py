from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Users(AbstractUser):
    class Role(models.TextChoices):
        SUPER_ADMIN = "SA", "superadmin",
        ADMIN = "AD", "admin",
        DELIVERY = "DV", "delivery",
        MERCHANT = "MCH", "merchant",
        CLIENT = "CL", "client"


    class Language(models.TextChoices):
        UZ = "UZB", "Uzbek"
        RU = "RUS", "Russian"
        EN = "ENG", "English"

    role = models.CharField(
        max_length=3,
        choices=Role.choices,
        default=Role.CLIENT,
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=50)
    telegram_id = models.PositiveIntegerField()
    step = models.IntegerField(default=0)
    language = models.CharField(
        max_length=3,
        choices=Language.choices,
        default=Language.UZ
    )


    def __str__(self):
        return f"{self.first_name} - {self.last_name} {self.role}"