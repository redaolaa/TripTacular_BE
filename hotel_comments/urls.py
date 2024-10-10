from django.urls import path
from .views import HotelCommentListView, HotelCommentDetailView

urlpatterns = [
    path('', HotelCommentListView.as_view()),
    path('<int:pk>/', HotelCommentDetailView.as_view())

]