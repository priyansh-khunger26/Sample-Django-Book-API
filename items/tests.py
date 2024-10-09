from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Book

class BookTests(APITestCase):
    def setUp(self):
        # Initial data setup for tests
        self.book_data = {
            "title": "Sample Book",
            "author": "John Doe",
            "published_date": "2020-01-01",
            "information": "1234567890123"
        }
        self.book = Book.objects.create(**self.book_data)
    
    def test_create_book(self):
        url = reverse('book-list')
        data = {
            "title": "New Book",
            "author": "Jane Smith",
            "published_date": "2021-06-15",
            "information": "9876543210987"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book.id})
        updated_data = {
            "title": "Updated Book",
            "author": "John Doe",
            "published_date": "2020-01-01",
            "information": "1234567890123"
        }
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")

    def test_delete_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
