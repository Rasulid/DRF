from django.test import TestCase
from django.urls import reverse
# Create your tests here.

from .models import Book


class BookTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="A good title",
            subtitle="A good subtitle",
            author="A good author",
            isbn="1234567890123"
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, "A good title")
        self.assertEqual(self.book.subtitle, "A good subtitle")
        self.assertEqual(self.book.author, "A good author")
        self.assertEqual(self.book.isbn, "1234567890123")

    def test_book_listview(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "A good subtitle")
        self.assertTemplateUsed(response, "book_list.html")
