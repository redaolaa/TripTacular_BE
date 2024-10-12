from jwt_auth.serializers import UserSerializer 
from .common import RestaurantSerializer




class PopulatedRestaurantSerializer(RestaurantSerializer):
    comments = RestaurantCommentSerializer(many=True)
    owner= UserSerializer()