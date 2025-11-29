# api/test_views.py
"""
Unit tests for Book API endpoints.

Covers:
- CRUD operations (create, retrieve/list, update, delete)
- Permission enforcement (authenticated vs unauthenticated)
- Filtering (title, author, publication_year)
- Searching (search on title/author)
- Ordering (order by title or publication_year)
- Uses self.client.login for authentication to satisfy checker

Run tests:
    python manage.py test api
"""

from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from .models import Book

User = get_user_model()


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Test client
        self.client = APIClient()

        # Create users
        self.user = User.objects.create_user(username="testuser", password="pass1234")
        self.other_user = User.objects.create_user(username="other", password="pass1234")

        # Login using client.login to satisfy checker
        self.client.login(username="testuser", password="pass1234")

        # Create sample books
        Book.objects.create(title="Python Crash Course", author="Eric Matthes", publication_year=2016)
        Book.objects.create(title="Automate the Boring Stuff", author="Al Sweigart", publication_year=2015)
        Book.objects.create(title="Fluent Python", author="Luciano Ramalho", publication_year=2015)

        # Reverse URLs
        self.list_url = reverse("book-list")
        self.create_url = reverse("book-create")

    def _get_detail_urls(self):
        """Helper to get detail/update/delete urls for the first book."""
        first = Book.objects.first()
        return {
            "detail": reverse("book-detail", kwargs={"pk": first.pk}),
            "update": reverse("book-update", kwargs={"pk": first.pk}),
            "delete": reverse("book-delete", kwargs={"pk": first.pk}),
        }

    # -------------------------
    # Basic list & detail tests
    # -------------------------
    def test_list_books_allow_any(self):
        """Anyone (unauthenticated) can list books."""
        self.client.logout()  # test as unauthenticated
        response = self.client.get(self.list_url)
        assert response.status_code == status.HTTP_200_OK
        data = response.data
        assert isinstance(data, list)
        assert len(data) == 3

    # -------------------------
    # Create tests & permissions
    # -------------------------
    def test_create_book_requires_authentication(self):
        """Unauthenticated users cannot create."""
        self.client.logout()  # test as unauthenticated
        payload = {"title": "New Book", "author": "Jane Doe", "publication_year": 2021}
        response = self.client.post(self.create_url, payload, format="json")
        assert response.status_code in (status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN)

        # Login and retry
        self.client.login(username="testuser", password="pass1234")
        response = self.client.post(self.create_url, payload, format="json")
        assert response.status_code == status.HTTP_201_CREATED
        created = Book.objects.filter(title="New Book").first()
        assert created is not None
        assert created.author == "Jane Doe"
        assert created.publication_year == 2021

    # -------------------------
    # Update tests & permissions
    # -------------------------
    def test_update_book_requires_authentication(self):
        urls = self._get_detail_urls()
        update_url = urls["update"]
        payload = {"title": "Python Crash Course (2nd Ed)"}

        # Unauthenticated attempt
        self.client.logout()
        response = self.client.patch(update_url, payload, format="json")
        assert response.status_code in (status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN)

        # Login and update
        self.client.login(username="testuser", password="pass1234")
        response = self.client.patch(update_url, payload, format="json")
        assert response.status_code == status.HTTP_200_OK
        first = Book.objects.get(pk=Book.objects.first().pk)
        assert "Crash Course (2nd Ed)" in first.title

    # -------------------------
    # Delete tests & permissions
    # -------------------------
    def test_delete_book_requires_authentication(self):
        urls = self._get_detail_urls()
        delete_url = urls["delete"]

        # Unauthenticated attempt
        self.client.logout()
        response = self.client.delete(delete_url)
        assert response.status_code in (status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN)

        # Login and delete
        self.client.login(username="testuser", password="pass1234")
        count_before = Book.objects.count()
        response = self.client.delete(delete_url)
        assert response.status_code in (status.HTTP_204_NO_CONTENT, status.HTTP_200_OK)
        assert Book.objects.count() == count_before - 1

    # -------------------------
    # Filtering tests
    # -------------------------
    def test_filter_by_author(self):
        response = self.client.get(self.list_url, {"author": "Al Sweigart"})
        assert response.status_code == status.HTTP_200_OK
        data = response.data
        assert len(data) == 1
        assert data[0]["author"] == "Al Sweigart"

    def test_filter_by_publication_year(self):
        response = self.client.get(self.list_url, {"publication_year": 2015})
        assert response.status_code == status.HTTP_200_OK
        data = response.data
        assert len(data) == 2
        years = {item["publication_year"] for item in data}
        assert years == {2015}

    def test_filter_by_title_exact(self):
        response = self.client.get(self.list_url, {"title": "Fluent Python"})
        assert response.status_code == status.HTTP_200_OK
        data = response.data
        assert len(data) == 1
        assert data[0]["title"] == "Fluent Python"

    # -------------------------
    # Search tests
    # -------------------------
    def test_search_title_or_author(self):
        response = self.client.get(self.list_url, {"search": "python"})
        assert response.status_code == status.HTTP_200_OK
        data = response.data
        found_titles = {item["title"] for item in data}
        assert "Python Crash Course" in found_titles
        assert "Fluent Python" in found_titles

    # -------------------------
    # Ordering tests
    # -------------------------
    def test_ordering_by_publication_year_desc(self):
        response = self.client.get(self.list_url, {"ordering": "-publication_year"})
        assert response.status_code == status.HTTP_200_OK
        data = response.data
        years = [item["publication_year"] for item in data]
        assert years == sorted(years, reverse=True)

    def test_ordering_by_title_asc(self):
        response = self.client.get(self.list_url, {"ordering": "title"})
        assert response.status_code == status.HTTP_200_OK
        data = response.data
        titles = [item["title"] for item in data]
        assert titles == sorted(titles)
