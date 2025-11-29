from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet
<<<<<<< HEAD
=======
from rest_framework.authtoken.views import obtain_auth_token
>>>>>>> 364e2dd (Setup Django project with DRF)

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
<<<<<<< HEAD
    path('', include(router.urls)),  # CRUD routes
=======
    path('', include(router.urls)),
    path('auth/token/', obtain_auth_token, name='api-token-auth'),
>>>>>>> 364e2dd (Setup Django project with DRF)
]
