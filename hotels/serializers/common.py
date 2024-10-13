from rest_framework import serializers
from ..models import Hotel
from hotel_comments.serializers.common import HotelCommentSerializer

class HotelSerializer(serializers.ModelSerializer):
    hotel_comments = HotelCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = ['id', 'name', 'stars', 'location', 'image_url', 'owner', 'hotel_comments']