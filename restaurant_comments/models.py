from django.db import models

# Create your models here.
class RestaurantComment(models.Model):
 

    def __str__(self):
        return f'{self.review} - {self.created_at}'
    review = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    restaurant = models.ForeignKey("restaurants.Restaurant", related_name="comments", on_delete=models.CASCADE)
    owner = models.ForeignKey('jwt_auth.User', related_name="restaurant_comments", on_delete=models.CASCADE)
    image_url = models.URLField(max_length=500, blank=True, null=True) 