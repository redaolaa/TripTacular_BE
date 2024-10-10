from django.urls import path
from .views import DestinationCommentListView, DestinationCommentDetailView

urlpatterns = [
    path('', DestinationCommentListView.as_view()),
    path('<int:pk>/', DestinationCommentDetailView.as_view())

]