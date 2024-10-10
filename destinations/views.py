from django.shortcuts import render
from rest_framework.views import APIView # this imports rest_frameworks APIView that we'll use to extend to our custom view
from rest_framework.response import Response # Response gives us a way of sending a http response to the user making the request, passing back data and other information
from rest_framework import status # status gives us a list of official/possible response codes

from .models import Destination
from .serializers import DestinationSerializer
# Create your views here.

class DestinationListView(APIView):

    def get(self, _request):
        destinations = Destination.objects.all()
        serialized_destinations = DestinationSerializer(destinations, many=True)
        return Response(serialized_destinations.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        destination_to_add = DestinationSerializer(data=request.data)
        try:
            destination_to_add.is_valid()
            destination_to_add.save()
            return Response(destination_to_add.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print("Error")
            return Response(e.__dict__ if e.__dict__ else str(e), status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class DestinationDetailView(APIView):
        def get_destination(self, pk):
            try:
                return Destination.objects.get(pk=pk)
            except Destination.DoesNotExist:
                raise NotFound(detail= "destination not found")


        def get(self, _request, pk):
            try:
                destination = self.get_destination(pk=pk)
                serialized_destination = DestinationSerializer(destination)
                return Response(serialized_destination.data, status=status.HTTP_200_OK)
            except Destination.DoesNotExist:
                raise NotFound(detail= "Destination not found")

        def put(self, request, pk):
            destination_to_update = self.get_destination(pk=pk)
            updated_destination = DestinationSerializer(destination_to_update, data=request.data)
            if updated_destination.is_valid():
                updated_destination.save()
                return Response(updated_destination.data, status=status.HTTP_202_ACCEPTED)
        
            return Response(updated_destination.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
        def delete(self, _request, pk):
             destination_to_delete = self.get_destination(pk=pk)
             destination_to_delete.delete()
             return Response(status=status.HTTP_204_NO_CONTENT)
