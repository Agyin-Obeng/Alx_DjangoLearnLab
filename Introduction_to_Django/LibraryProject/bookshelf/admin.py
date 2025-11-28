from django.contrib import admin
from .models import Book

# Customize admin display
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # fields to display in list view
    search_fields = ('title', 'author')                      # enable search by title and author
    list_filter = ('publication_year',)                     # filter by publication year

# Register with the custom admin
admin.site.register(Book, BookAdmin)
