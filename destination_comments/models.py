from django.db import models

# Create your models here.
class DestinationComment(models.Model):
 

    def __str__(self):
        return f'{self.review} - {self.created_at}'
    review = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    destination = models.ForeignKey("destinations.Destination", related_name="comments", on_delete=models.CASCADE)