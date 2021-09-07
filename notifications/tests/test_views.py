from django.contrib.auth.models import User
from django.http import response
from django.test import TestCase
from django.urls import reverse

from notifications.models import Notification


class NotificationListTestCase(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        # Create a user
        cls.test_user1 = User.objects.create_user(
            username="test_user1", password="test_pass1"
        )
        cls.test_user1.save()
        cls.test_user2 = User.objects.create_user(
            username="test_user2", password="test_pass2"
        )
        cls.test_user2.save()
        Notification.objects.create(
            title="Notification title1",
            message="Notification message1",
            user=cls.test_user1,
        )
        Notification.objects.create(
            title="Notification title2",
            message="Notification message2",
            user=cls.test_user2,
        )

    def test_notification_list_url(self):
        self.client.login(username="test_user1", password="test_pass1")
        notifications = (
            Notification.objects.filter(user=self.test_user1)
            .all()
            .order_by("-notification_at")
        )
        self.assertEqual(notifications.count(), 2)
        response = self.client.get(reverse("notifications:notification-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTrue("notifications" in response.context)
        self.assertTemplateUsed(response, "notifications/notification_list.html")

    def test_notification_detail_url(self):
        self.client.login(username="test_user1", password="test_pass1")
        response = self.client.get(
            reverse("notifications:notification-detail", kwargs={"notification_id": 3})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue("notification" in response.context)
        self.assertTemplateUsed(response, "notifications/notification_detail.html")

    def test_notification_delete_url(self):
        self.client.login(username="test_user1", password="test_pass1")
        response = self.client.get(
            reverse("notifications:notification-delete", kwargs={"notification_id": 3})
        )
        self.assertRedirects(response, "/notifications/")
