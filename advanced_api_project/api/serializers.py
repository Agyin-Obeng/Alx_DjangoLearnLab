from rest_framework import serializers
from .models import Author, Book
from datetime import datetime


# Serializer for Book model
class BookSerializer(serializers.ModelSerializer):

    # Custom validation to ensure publication_year is never in the future
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']


# Serializer for Author, including nested books
class AuthorSerializer(serializers.ModelSerializer):
    # Nested serializer: shows all books under this author
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
        # The relationship is handled using the "related_name='books'" in the model
