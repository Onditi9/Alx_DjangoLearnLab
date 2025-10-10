from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post-list'),  # Example
]

from django.urls import path
from .views import FeedView

urlpatterns = [
    path('feed/', FeedView.as_view(), name='feed'),
]

from django.urls import path
from .views import FeedView, LikePostView, UnlikePostView, PostLikesListView

urlpatterns = [
    path('feed/', FeedView.as_view(), name='feed'),
    path('<int:pk>/like/', LikePostView.as_view(), name='post-like'),
    path('<int:pk>/unlike/', UnlikePostView.as_view(), name='post-unlike'),
    path('<int:pk>/likes/', PostLikesListView.as_view(), name='post-likes'),
]
