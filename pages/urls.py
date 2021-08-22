from django.urls import path

from pages.views.faq_view import faq_view

app_name = "pages"

urlpatterns = [
    path("", faq_view, name="faqs"),
]
