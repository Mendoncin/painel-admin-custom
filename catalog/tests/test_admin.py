from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSiteTests(TestCase):
    def setUp(self):
        self.client = Client()
        # Create a superuser for testing
        self.admin_user = get_user_model().objects.create_superuser(
            username='admin',
            password='adminpassword'
        )
        self.client.force_login(self.admin_user)
        self.author = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword',
            psedonimo='test pseudonym'
        )

    def test_author_pseudym_list(self):
        """"
        Test that the author's pseudonym is displayed in the admin list view.
        :return:
        """
        url = reverse('admin:catalog_author_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.author.psedonimo)

    def test_author_detail_pseudonym_list(self):
        """
        Test that the author's pseudonym is displayed in the admin detail view.
        :return:
        """
        url = reverse('admin:catalog_author_change', args=[self.author.id])
        res = self.client.get(url)

        self.assertContains(res, self.author.psedonimo)