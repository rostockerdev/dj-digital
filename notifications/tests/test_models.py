from django.contrib.auth.models import User
from django.http import response
from django.test import TestCase
from django.urls import reverse

from notifications.models import Notification


class NotificationModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        # Create a user
        cls.test_user = User.objects.create_user(
            username="test_user", password="test_pass"
        )
        cls.test_user.save()
        cls.notifications_1 = Notification.objects.create(
            title="Notification title",
            message="Notification message",
            user=cls.test_user,
        )

    def test_notification_model_instance(self):
        obj = Notification.objects.get(id=2)
        self.assertEqual(str(obj.title), "Notification title")
