from django.urls import path
from .views import FollowUserView, UnfollowUserView, UserListView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:user_id>/follow/', FollowUserView.as_view(), name='follow-user'),
    path('users/<int:user_id>/unfollow/', UnfollowUserView.as_view(), name='unfollow-user'),
]
