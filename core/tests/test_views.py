from django.http import response
from django.test import SimpleTestCase
from django.urls import reverse

from core.views.home_view import home_view


class HomePageTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_view_url_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_home_view_use_correct_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "pages/home.html")
