from django.test import Client, TestCase
from django.urls import reverse


class TestPage(TestCase):

    def setUp(self):
        self.client = Client()

    def test_index(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'oc_lettings_site/index.html')
        self.assertContains(response, "<title>Holiday Homes</title>")
