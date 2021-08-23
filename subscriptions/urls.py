from django.urls import path

from subscriptions import views as sub_view

app_name = "subscriptions"

urlpatterns = [
    path("", sub_view.subscription_view, name="subscribe"),
    path(
        "confirm/", sub_view.subscription_confirmation, name="subscription-confirmation"
    ),
]
