from django.test import TestCase
from django.urls import reverse


class SearchQueryViewTestCase(TestCase):
    def setUp(self) -> None:
        pass

    def test_search_empty_query_url(self):
        response = self.client.get("/search/", kwargs={"q": ""})
        self.assertTrue(response.status_code, 302)
        self.assertRedirects(response, "/")

    def test_search_with_query_url(self):
        response = self.client.get("/search/", kwargs={"q": ""})
        self.assertTrue(response.status_code, 302)
        self.assertRedirects(response, "/")
