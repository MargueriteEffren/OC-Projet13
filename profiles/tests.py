from django.test import Client, TestCase
from django.urls import reverse
from profiles.models import Profile
from django.contrib.auth.models import User


class TestPage(TestCase):

    def setUp(self):
        self.client = Client()

    def test_profiles_index(self):
        url = reverse('profiles_index', current_app='profiles')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profiles_index.html')
        self.assertContains(response, "<title>Profiles</title>")

    def test_profile(self):
        user = User.objects.create(
            username="John",
            first_name="John",
            last_name="Grease",
        )
        profile = Profile.objects.create(
            user=user,
            favorite_city="Rome",

        )  # création d'une fausse database pour le test avec un objet
        # User et un objet Profile (on aurait aussi pu utiliser
        # pytest.fixtures - voir cours OC
        # https://openclassrooms.com/fr/courses/7155841-testez-votre-projet-python/7414196-utilisez-les-fixtures)

        url = reverse('profile', kwargs={'username': profile.user.username})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertContains(response, 'Rome')
