from django.test import Client, TestCase
from django.urls import reverse
from lettings.models import Address, Letting


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
            zip_code="99999",
            country_iso_code="USA"
        )
        letting = Letting.objects.create(
            title="the famous House",
            address=address
        )  # création d'une fausse database pour le test avec un objet
        # Address et un objet Letting (on aurait aussi pu utiliser
        # pytest.fixtures - voir cours OC
        # https://openclassrooms.com/fr/courses/7155841-testez-votre-projet-python/7414196-utilisez-les-fixtures)

        url = reverse('letting', kwargs={'letting_id': letting.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/letting.html')
        self.assertContains(response, 'Beverly Hills')
