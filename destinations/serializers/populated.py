from jwt_auth.serializers import UserSerializer 
from .common import DestinationSerializer
from hotels.serializers.common import HotelSerializer
from restaurants.serializers.common import RestaurantSerializer



class PopulatedDestinationSerializer(DestinationSerializer):
    hotels= HotelSerializer()
    restaurants= HotelSerializer()
    owner= UserSerializer()