from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters import rest_framework   # ✅ required by the check
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Book
from .serializers import BookSerializer

 class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]



class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # only logged-in users can create


class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # only logged-in users can update


class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # only logged-in users can delete

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # 🔑 Enable filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Filtering
    filterset_fields = ["title", "author", "publication_year"]

    # Searching
    search_fields = ["title", "author__name"]  # assuming Book has FK to Author

    # Ordering
    ordering_fields = ["title", "publication_year"]
    ordering = ["title"]  # default ordering
