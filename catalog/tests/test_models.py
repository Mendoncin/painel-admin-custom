from django.test import TestCase

from catalog.models import LiteraryFormat
from catalog.models import Book
from django.contrib.auth import get_user_model


# Create your tests here.

class ModelTests(TestCase):
    def test_literary_format_str(self):
        literary_format = LiteraryFormat(name="test")
        self.assertEqual(str(literary_format), "test")

    def test_author_str(self):
        author = get_user_model().objects.create(
            username="testuser",
            first_name="test",
            last_name="one",
            psedonimo="test pseudonym",
        )
        self.assertEqual(
            str(author),
            f"{author.first_name} {author.last_name}"
        )

    def test_book_str(self):
        literary_format = LiteraryFormat(name="test")
        literary_format.save()
        author = get_user_model().objects.create(
            username="testuser",
            first_name="test",
            last_name="one",
            psedonimo="test pseudonym",
        )
        book = Book.objects.create(
            title="Test Book",
            price=19.99,
            format=literary_format
        )
        book.authors.add(author)
        self.assertEqual(
            str(book),
            f"{book.title} (price: {book.price}, format: {book.format})"
        )

    def test_create_author_with_pseudonym(self):
        username = "testuser"
        password = "testpassword"
        psedonimo = "test pseudonym"
        author = get_user_model().objects.create_user(
            username=username,
            password=password,
            psedonimo=psedonimo,
        )
        self.assertEqual(author.psedonimo, psedonimo)
        self.assertEqual(author.username, username)
        self.assertTrue(author.check_password(password))