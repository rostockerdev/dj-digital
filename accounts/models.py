from datetime import datetime

import stripe
from decouple import config
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from memberships.models import Membership

stripe.api_key = settings.STRIPE_SECRET_KEY


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )
    membership = models.ForeignKey(
        "memberships.Membership", on_delete=models.SET_NULL, null=True
    )
    stripe_customer_id = models.CharField(max_length=100)
    profile_pic = ProcessedImageField(
        default="avatar.jpg",
        upload_to="profile-pic/",
        processors=[ResizeToFill(200, 200)],
        format="JPEG",
        options={"quality": 60},
    )

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"


class Subscription(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    stripe_subscription_id = models.CharField(max_length=50)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Subscription"
        verbose_name_plural = "Subscriptions"

    def __str__(self):
        return self.profile.user.username
