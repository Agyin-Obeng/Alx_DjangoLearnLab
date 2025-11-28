from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('relationship_app.urls')),
    path('', RedirectView.as_view(url='/login/', permanent=False)),  # Root redirects to login
]


from django.urls import path
from .views.admin_view import admin_view

urlpatterns = [
    path('admin/', admin_view, name='admin_view'),
]


from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # for your custom register_view

urlpatterns = [
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register_view, name='register'),  # your custom registration view
]






