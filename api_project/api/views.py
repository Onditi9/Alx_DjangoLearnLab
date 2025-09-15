from rest_framework import generics
from .models import Book
from .import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()       # all books from the DB
    serializer_class = BookSerializer   # serialize them into JSON



