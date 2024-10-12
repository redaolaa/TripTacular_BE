from rest_framework import serializers
from ..models import Restaurant
from destinations.serializers.common import DestinationSerializer 
from restaurant_comments.serializers.common import RestaurantCommentSerializer 

class RestaurantSerializer(serializers.ModelSerializer):
    destination = DestinationSerializer()
    comments = RestaurantCommentSerializer(many=True, required=False, allow_null=True)
    class Meta:
        model = Restaurant
        fields = '__all__' 