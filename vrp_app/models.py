# vrp_app/models.py

from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    x = models.FloatField()  # Latitude
    y = models.FloatField()  # Longitude

    def __str__(self):
        return f"{self.name} ({self.x}, {self.y})"

class Vehicle(models.Model):
    capacity = models.IntegerField()

    def __str__(self):
        return f"Vehicle with capacity {self.capacity}"
