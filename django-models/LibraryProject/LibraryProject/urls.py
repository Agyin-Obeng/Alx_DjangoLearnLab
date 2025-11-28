from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("books/", include("book_store.urls")),
    path("admin/", admin.site.urls),
]

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('relationship_app.urls')),
    path('', RedirectView.as_view(url='/login/', permanent=False)),  # Root redirects to login
    path('', include('relationship_app.urls')),

]


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin-django/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
]
