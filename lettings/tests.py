from .views import lettings_index
from django.test import Client, TestCase
from django.urls import reverse
from lettings.models import Address, Letting


#TODO : effacer ce test
def test_dummy():
    assert 1


class TestPage(TestCase):

    def setUp(self):
        self.client = Client()

    def test_lettings_index(self):
        url = reverse('lettings_index', current_app='lettings')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/lettings_index.html')
        self.assertContains(response, "<title>Lettings</title>")

    def test_lettings(self):
        address = Address.objects.create(
            number=90210,
            street="Beverly Hills",
            city="Los Angeles",
            state='CA',
            zip_code="some_zip",
            country_iso_code="USA"
        )
        letting = Letting.objects.create(
            title="the famous House",
            address=address
        )

        url = reverse('letting', kwargs={'letting_id': letting.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/letting.html')
        self.assertContains(response, 'Joy Ridge Street')
