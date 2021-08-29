from django.http import response
from django.test import SimpleTestCase
from django.urls import reverse

from pages.views.faq_view import faq_view


class FaqPageTests(SimpleTestCase):
    def test_faq_page_status_code(self):
        response = self.client.get("faqs/")
        self.assertEquals(response.status_code, 200)

    def test_faq_view_url_by_name(self):
        response = self.client.get(reverse("pages:faqs"))
        self.assertEquals(response.status_code, 200)

    def test_faq_view_use_correct_template(self):
        response = self.client.get(reverse("pages:faqs"))
        self.assertTemplateUsed(response, "pages/faqs.html")
