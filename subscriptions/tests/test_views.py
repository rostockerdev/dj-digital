import datetime
from re import I

from django.test import RequestFactory, TestCase
from django.urls import reverse
from requests.api import request

from subscriptions.emailutility.email_utility import send_subscription_email
from subscriptions.encodeutility.enc_dec_util import decrypt, encrypt
from subscriptions.models import Subscribe
from subscriptions.validation_utility import validate_email
from subscriptions.views.subscription_view import save_email


class SubscribeViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.SUBSCRIBE_STATUS = "subscribed"
        cls.SEPARATOR = "&"
        cls.subscribe_test = Subscribe.objects.create(email="testemail@gmail.com")

    def test_subscribe_view_url(self):
        self.client.get("subscriptions:subscribe")
        # Test wrong email without @
        test_email_without_at = "testemailgmail.com"
        error_msg_without_at = validate_email(test_email_without_at)
        self.assertEqual(error_msg_without_at, "Invalid Email Address.")

        # Test wrong email without .
        test_email_without_dot = "testemail@gmailcom"
        error_msg_without_dot = validate_email(test_email_without_dot)
        self.assertEqual(error_msg_without_dot, "Invalid Email Address.")

        test_email_data = "testemail@gmail.com"
        save_status = save_email(test_email_data)
        self.assertTrue(save_status, True)

        # Create test token
        test_token = encrypt(test_email_data + self.SEPARATOR + str(datetime.time()))
        print(test_token)

        # Create subscription confirmation url
        self.factory = RequestFactory()
        test_subscription_confirmation_url = self.factory.get(
            f"/subscriptions/confirm/?token={test_token}"
        )

        send_subscription_email(test_email_data, test_subscription_confirmation_url)
