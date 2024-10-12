from rest_framework import serializers
from ..models import Hotel
from destinations.serializers.common import DestinationSerializer 
from hotel_comments.serializers.common import HotelCommentSerializer 

class HotelSerializer(serializers.ModelSerializer):
    destination = DestinationSerializer()
    comments = HotelCommentSerializer(many=True, required=False, allow_null=True)


    class Meta:
        model = Hotel
        fields = '__all__' 