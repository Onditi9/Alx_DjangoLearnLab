from rest_framework import serializers
from . import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'   # include all fields from the model
