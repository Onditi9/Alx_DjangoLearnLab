from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Book
from . import BookSerializer
from .serializers import BookSerializer
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    (list, create, retrieve, update, destroy) for Book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer






