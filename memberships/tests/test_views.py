from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from memberships.models import Membership


class MembershipViewTestCase(TestCase):
    """Test the Dashboard View"""

    def setUp(self) -> None:
        # Create a user
        self.test_user = User.objects.create_user(
            username="test_user", password="test_pass"
        )
        self.membership_free = Membership.objects.create(
            slug="free",
            # membership_type='Free',
            stripe_plan_id="Free101",
            price=10.00,
        )

    def test_dashboard_for_anonymous_user_url_(self):
        response = self.client.get(reverse("memberships:dashboard"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/dashboard/")

    def test_dashboard_for_logged_in_user_url_(self):
        self.client.login(username="test_user", password="test_pass")
        response = self.client.get(reverse("memberships:dashboard"))
        # Check user is logged in
        self.assertEqual(str(response.context["user"]), "test_user")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "memberships/dashboard.html")
