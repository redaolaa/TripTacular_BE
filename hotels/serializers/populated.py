from jwt_auth.serializers import UserSerializer 
from .common import DestinationSerializer




class PopulatedHotelSerializer(HotelSerializer):
    owner= UserSerializer()