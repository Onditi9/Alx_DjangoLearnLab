from rest_framework import viewsets
from .models import Book
from . import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    (list, create, retrieve, update, destroy) for Book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer




