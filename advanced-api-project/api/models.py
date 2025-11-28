from django.db import models

# Author model stores writer information.
class Author(models.Model):
    # Name of the author
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Book model stores book information and links each book to an author.
class Book(models.Model):
    # Title of the book
    title = models.CharField(max_length=255)

    # Year the book was published
    publication_year = models.IntegerField()

    # Foreign key creates a one-to-many relation:
    # One Author ➜ Many Books
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
