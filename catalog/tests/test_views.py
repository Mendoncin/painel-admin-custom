from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from catalog.models import LiteraryFormat

LITERARY_FORMAT_URL = reverse("catalog:lista-de-generos")

class PublicLiteraryFormatTest(TestCase):
    def test_login_required(self):
        res = self.client.get(LITERARY_FORMAT_URL)
        self.assertNotEqual(res.status_code, 200)

class PrivateLiteraryFormatTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="testpassword"
        )
        self.client.force_login(self.user)

    def test_retrieve_literary_formats(self):
        LiteraryFormat.objects.create(name="Ficção Científica")
        LiteraryFormat.objects.create(name="Romance")
        response = self.client.get(LITERARY_FORMAT_URL)
        self.assertEqual(response.status_code, 200)
        literary_formats = LiteraryFormat.objects.all()
        self.assertEqual(list(response.context["genres"]), list(literary_formats))

        self.assertTemplateUsed(response, "catalog/genres_list.html")
