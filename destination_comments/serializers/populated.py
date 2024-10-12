from jwt_auth.serializers import UserSerializer 
from .common import DestinationCommentSerializer




class PopulatedDestinationCommentSerializer(DestinationCommentSerializer):
    owner= UserSerializer()