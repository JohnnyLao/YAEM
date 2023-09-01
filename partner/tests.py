from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse


class PartnerTests(TestCase):
    def test_partner_page(self):
        path = reverse("partner:partner_page")
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
