from django.contrib import admin
from django.urls import path, include
from .views import home  # import the home view

urlpatterns = [
    path('', home),  # root path
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
]
