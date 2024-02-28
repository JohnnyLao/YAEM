from django.test import TestCase
from django.urls import reverse
from rest_framework import status


class TestBanquet(TestCase):
    def test_page_is_open(self):
        response = self.client.get(reverse('banquets:banquet_list_page'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)