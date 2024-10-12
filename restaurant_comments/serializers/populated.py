from jwt_auth.serializers import UserSerializer 
from .common import RestaurantCommentSerializer




class PopulatedRestaurantCommentSerializer(RestaurantCommentSerializer):
    owner= UserSerializer()