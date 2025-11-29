<<<<<<< HEAD
=======
from rest_framework.permissions import IsAuthenticated, IsAdminUser
>>>>>>> 364e2dd (Setup Django project with DRF)
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
<<<<<<< HEAD
=======
    permission_classes = [IsAdminOrReadOnly]
  # restrict access to authenticated users only

from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        return request.user and request.user.is_staff



>>>>>>> 364e2dd (Setup Django project with DRF)
