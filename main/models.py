from django.db import models
from django.utils import timezone
# Create your models here.


class User(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name


class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.CharField(max_length=200, blank=True, null=True)
  

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    order_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.full_name} - {self.food_item.name}"
