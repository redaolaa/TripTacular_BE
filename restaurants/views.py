from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Restaurant
from .serializers.common import RestaurantSerializer

class RestaurantListView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, request):
        restaurants = Restaurant.objects.all()
        serialized_restaurants = RestaurantSerializer(restaurants, many=True)
        return Response(serialized_restaurants.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        restaurant_to_add = RestaurantSerializer(data=request.data)
        if restaurant_to_add.is_valid():
            restaurant_to_add.save()
            return Response(restaurant_to_add.data, status=status.HTTP_201_CREATED)
        return Response(restaurant_to_add.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class RestaurantDetailView(APIView):

    def get_restaurant(self, pk):
        try:
            return Restaurant.objects.get(pk=pk)
        except Restaurant.DoesNotExist:
            raise NotFound(detail="Restaurant not found")

    def get(self, request, pk):
        restaurant = self.get_restaurant(pk)
        serialized_restaurant = RestaurantSerializer(restaurant)
        return Response(serialized_restaurant.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        restaurant_to_update = self.get_restaurant(pk)
        updated_restaurant = RestaurantSerializer(restaurant_to_update, data=request.data)
        if updated_restaurant.is_valid():
            updated_restaurant.save()
            return Response(updated_restaurant.data, status=status.HTTP_202_ACCEPTED)
        return Response(updated_restaurant.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, request, pk):
        restaurant_to_delete = self.get_restaurant(pk)
        restaurant_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)