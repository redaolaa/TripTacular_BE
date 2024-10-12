from rest_framework import serializers
from ..models import Destination
from destination_comments.serializers.common import DestinationCommentSerializer 

class DestinationSerializer(serializers.ModelSerializer):
    comments = DestinationCommentSerializer(many=True, required=False, allow_null=True)
    class Meta:
      model = Destination
      fields = '__all__'

