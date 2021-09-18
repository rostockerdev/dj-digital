from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

import stripe
from decouple import config
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from memberships.models import Membership

stripe.api_key = settings.STRIPE_SECRET_KEY


class Profile(models.Model):
    """Model representing Profile."""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )
    membership = models.ForeignKey(
        "memberships.Membership", on_delete=models.SET_NULL, null=True
    )
    stripe_customer_id = models.CharField("Stripe Customer ID", max_length=128)
    profile_pic = ProcessedImageField(
        default="avatar.jpg",
        upload_to="profile-pic/",
        processors=[ResizeToFill(200, 200)],
        format="JPEG",
        options={"quality": 60},
    )

    def __str__(self):
        """String for representing the Model object"""
        return self.user.username

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"


class Subscription(models.Model):
    """Model representing Subscription Instance."""

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    stripe_subscription_id = models.CharField("Stripe Subscription ID", max_length=128)
    is_active = models.BooleanField("Subscription Status", default=True)

    class Meta:
        verbose_name = "Subscription"
        verbose_name_plural = "Subscriptions"

    def __str__(self):
        """String for representing the Model object"""
        return self.profile.user.username

    @property
    def get_next_billing_date(self):
        subscription = stripe.Subscription.retrieve(self.stripe_subscription_id)
        return datetime.fromtimestamp(subscription.current_period_end)
