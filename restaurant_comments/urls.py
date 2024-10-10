from django.urls import path
from .views import RestaurantCommentListView, RestaurantCommentDetailView

urlpatterns = [
    path('', RestaurantCommentListView.as_view()),
    path('<int:pk>/', RestaurantCommentDetailView.as_view())

]