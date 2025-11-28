# api/views.py

from rest_framework import generics, permissions, filters
from rest_framework.exceptions import ValidationError
from .models import Book
from .serializers import BookSerializer

# ------------------------------
# List all books (readable by anyone)
# Supports search and ordering
# ------------------------------
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author__name']
    ordering_fields = ['publication_year', 'title']

# ------------------------------
# Retrieve a single book (readable by anyone)
# ------------------------------
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# ------------------------------
# Create a new book (authenticated users only)
# Custom validation for publication year
# ------------------------------
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Additional logic can go here, e.g., log creator
        serializer.save()

    def create(self, request, *args, **kwargs):
        # Validate that publication_year is not in the future
        publication_year = request.data.get('publication_year')
        if publication_year and int(publication_year) > 2025:  # Update 2025 to current year if needed
            raise ValidationError({"publication_year": "Cannot be in the future"})
        return super().create(request, *args, **kwargs)

# ------------------------------
# Update an existing book (authenticated users only)
# Prevent changing the author
# ------------------------------
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        # Prevent updating the author
        if 'author' in request.data:
            request.data.pop('author')
        return super().update(request, *args, **kwargs)

# ------------------------------
# Delete a book (authenticated users only)
# ------------------------------
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# BookListView: Lists all books, readable by anyone.
# BookDetailView: Retrieve a single book by its primary key.
# BookCreateView: Create a new book, authenticated users only.
# BookUpdateView: Update an existing book, authenticated users only.
# BookDeleteView: Delete a book, authenticated users only.
