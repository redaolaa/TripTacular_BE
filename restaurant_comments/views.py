from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import RestaurantComment
from .serializers import RestaurantCommentSerializer

class RestaurantCommentListView(APIView):

    def get(self, request):
        comments = RestaurantComment.objects.all()
        serialized_comments = RestaurantCommentSerializer(comments, many=True)
        return Response(serialized_comments.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        comment_to_add = RestaurantCommentSerializer(data=request.data)
        if comment_to_add.is_valid():
            comment_to_add.save()
            return Response(comment_to_add.data, status=status.HTTP_201_CREATED)
        return Response(comment_to_add.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class RestaurantCommentDetailView(APIView):

    def get_comment(self, pk):
        try:
            return RestaurantComment.objects.get(pk=pk)
        except RestaurantComment.DoesNotExist:
            raise NotFound(detail="Comment not found")

    def get(self, request, pk):
        comment = self.get_comment(pk)
        serialized_comment = RestaurantCommentSerializer(comment)
        return Response(serialized_comment.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        comment_to_update = self.get_comment(pk)
        updated_comment = RestaurantCommentSerializer(comment_to_update, data=request.data)
        if updated_comment.is_valid():
            updated_comment.save()
            return Response(updated_comment.data, status=status.HTTP_202_ACCEPTED)
        return Response(updated_comment.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, request, pk):
        comment_to_delete = self.get_comment(pk)
        comment_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)