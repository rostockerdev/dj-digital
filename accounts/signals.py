import stripe
from decouple import config
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from memberships.models import Membership

from .models import Profile

stripe.api_key = config("STRIPE_SECRET_KEY")


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile_membership(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)

    profile, created = Profile.objects.get_or_create(user=instance)

    if profile.stripe_customer_id is None or profile.stripe_customer_id == "":
        new_customer_id = stripe.Customer.create(email=instance.email)
        try:
            free_membership = Membership.objects.get(membership_type="Free")
        except Membership.DoesNotExist:
            free_membership = None
        profile.stripe_customer_id = new_customer_id["id"]
        profile.membership = free_membership
        # profile.membership = 'Free'
        profile.save()
