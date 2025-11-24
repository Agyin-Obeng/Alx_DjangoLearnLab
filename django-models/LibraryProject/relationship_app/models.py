from django.db import models

# Author can write many books
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# A Book belongs to one Author
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# A Library has many Books (and Books can be in many Libraries)
class Library(models.Model):
    name = models.CharField(max_length=150)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name


# A Librarian belongs to ONE library
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
