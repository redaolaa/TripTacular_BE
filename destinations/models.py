from django.db import models
from datetime import date

# Create your models here.
class Destination(models.Model):
  def __str__(self):
    return f'{self.city} - {self.country}'
  country = models.CharField(max_length=80)
  city = models.CharField(max_length=50)
  date_from = models.DateField(default=date.today)
  date_to = models.DateField(default=date.today)