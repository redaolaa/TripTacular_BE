from rest_framework import serializers
from .models import DestinationComment

class DestinationCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DestinationComment
        fields = '__all__' 