from django.db import models

# Create your models here.


# Simple User Model (for signup)
class User(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


# Home page ke food items (6 item display)
class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.CharField(max_length=200)   # simple URL rakh rahe hai

    def __str__(self):
        return self.name
