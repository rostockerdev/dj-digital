from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

from courses.models import Course


class Notification(models.Model):
    title = models.CharField(max_length=256)
    message = models.TextField()
    viewed = models.BooleanField(default=False)
    notification_at = models.DateTimeField(
        verbose_name="Notification Create At", auto_now_add=True, null=True
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_read_url(self):
        return reverse(
            "notifications:notification-detail", kwargs={"notification_id": self.id}
        )

    def get_notification_url(self):
        return reverse(
            "notifications:notification-detail", kwargs={"notification_id": self.id}
        )


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_coursenotification_message(sender, *args, **kwargs):
    if kwargs.get("created", False):
        Notification.objects.create(
            user=kwargs.get("instance"),
            title="Welcome to Rostocker Labs Digital Services",
            message="Thank you for signing up",
        )
