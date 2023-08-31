from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse


class CartTests(TestCase):
    def test_cart_page(self):
        path = reverse("cart:cart_page")
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
