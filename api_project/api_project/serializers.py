from rest_framework import serializers
from .models import Book   # import your Book model

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'   # include all model fields

