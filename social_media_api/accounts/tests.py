from django.test import TestCase

# Create your tests here.

from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post-list'),  # Example
]
