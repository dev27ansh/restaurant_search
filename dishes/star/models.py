
from django.db import models
import json

class Restaurant(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    lat_long = models.CharField(max_length=50)
    full_details = models.TextField()

    def __str__(self):
        return self.name

class Item(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} - {self.restaurant.name}"
