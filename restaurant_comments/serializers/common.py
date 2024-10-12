from rest_framework import serializers
from ..models import RestaurantComment

class RestaurantCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantComment
        fields = '__all__' 