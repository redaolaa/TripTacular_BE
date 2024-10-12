from jwt_auth.serializers import UserSerializer 
from .common import HotelCommentSerializer




class PopulatedHotelCommentSerializer(HotelCommentSerializer):
    owner= UserSerializer()