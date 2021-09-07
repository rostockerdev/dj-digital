from django.contrib.auth.models import User
from django.test import TestCase

from accounts.models import Profile, Subscription
from memberships.models import Membership


class ProfileModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.test_user = User.objects.create_user(
            username="test_user", password="test_password"
        )
        cls.test_user.save()
        Membership.objects.create(
            slug="free",
            membership_type="Free",
            stripe_plan_id="Free101",
            price=10.00,
        )
        # Profile.objects.create(
        #     user=test_user,
        #     membership = membership_free,
        #     stripe_customer_id = STRIPE_CUSTOMER_ID,
        #     profile_pic = 'profile-pic/avatar.jpg'
        # )

    def test_profile_object_representation(self):
        obj = Profile.objects.get(id=1)
        self.assertEqual(obj.user.username, "test_user")

    def test_profile_model_data(self):
        obj = Profile.objects.get(id=1)
        self.assertEqual(obj.profile_pic, "avatar.jpg")


class SubscriptionModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.STRIPE_SUBSCRIPTION_ID = "STRIPE_001"
        cls.test_user = User.objects.create_user(
            username="test_user", password="test_password"
        )
        cls.test_user.save()
        cls.test_profile = Profile.objects.get(id=1)
        Subscription.objects.create(
            profile=cls.test_profile, stripe_subscription_id=cls.STRIPE_SUBSCRIPTION_ID
        )

    def test_subscription_model_object_representation(self):
        obj = Subscription.objects.get(id=1)
        self.assertEqual(obj.profile.user.username, "test_user")

    def test_subscription_model_data(self):
        obj = Subscription.objects.get(id=1)
        self.assertEqual(obj.stripe_subscription_id, self.STRIPE_SUBSCRIPTION_ID)
        self.assertEqual(obj.is_active, True)
