from django.urls import path
from .views import HotelListView, HotelDetailView

urlpatterns = [
    path('', HotelListView.as_view()),
    path('<int:pk>/', HotelDetailView.as_view())

]