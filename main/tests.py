from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from main.models import City, Client


class MainTests(TestCase):
    def setUp(self):
        self.city_test_model = City.objects.create(
            name="TestCity",
            slug="test_slug",
        )

        self.client_test_model = Client.objects.create(
            name="Test Client",
            city=self.city_test_model,
            logo="media/Turan/logo/logoturan.jpg",
            description="Test Description",
            working_time="00:00",
            address="Test Address",
            phone="777777777",
            status=True,
            outside=True,
            delivery=True,
            url_name="test_url",
        )

    def test_get_main_page(self):
        path = reverse("main:main_page")
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_get_menu_page(self):
        url_name = self.client_test_model.url_name
        path = reverse("main:menu_page", kwargs={"url_name": url_name})
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_get_city_filter(self):
        slug = self.city_test_model.slug
        path = reverse("main:city_filter", kwargs={"city_slug": slug})
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
