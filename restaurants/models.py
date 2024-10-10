from django.db import models

# Create your models here.
class Restaurant(models.Model):
    PRICE_RANGES = [
        ('0-10', '0-10'),
        ('10-20', '10-20'),
        ('20-30', '20-30'),
        ('30-40', '30-40'),
        ('40+', '40+')
    ]

    def __str__(self):
        return f'{self.name} - {self.location}'
    name = models.CharField(max_length=200)
    cuisine = models.CharField(max_length=100)
    location = models.CharField(max_length=250)
    price_range = models.CharField(max_length=5, choices= PRICE_RANGES, default='0-10')
    destination = models.ForeignKey("destinations.Destination", related_name="restaurants", on_delete=models.CASCADE)