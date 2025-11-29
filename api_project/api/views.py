from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# NEW — CRUD ViewSet
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
