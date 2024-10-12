from rest_framework import serializers
from ..models import HotelComment

class HotelCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelComment
        fields = '__all__' 