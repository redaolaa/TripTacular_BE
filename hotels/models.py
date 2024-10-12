from django.db import models

# Create your models here.
class Hotel(models.Model):
    def __str__(self):
        return f'{self.name} - {self.location}'
    name = models.CharField(max_length=200)
    stars = models.CharField(max_length=5)
    location = models.CharField(max_length=250)
    destination = models.ForeignKey("destinations.Destination", related_name="hotels", on_delete=models.CASCADE)
    owner = models.ForeignKey('jwt_auth.User', related_name="hotels", on_delete=models.CASCADE)
    image_url = models.URLField(max_length=500, blank=True, null=True) 