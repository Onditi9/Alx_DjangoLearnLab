from django.urls import path
from .views import FollowUserView, UnfollowUserView

urlpatterns = [
    path('follow/<int:pk>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:pk>/', UnfollowUserView.as_view(), name='unfollow-user'),
]
