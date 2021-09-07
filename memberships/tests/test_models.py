from django.test import TestCase

from memberships.models import Membership


class MembershipTestCase(TestCase):
    """Test the Membership instance"""

    def setUp(self) -> None:
        self.membership_free = Membership.objects.create(
            slug="free",
            # membership_type='Free',
            stripe_plan_id="Free101",
            price=10.00,
        )

    def test_membership_model_instance(self):
        obj = Membership.objects.get(id=1)
        self.assertEqual(obj.membership_type, self.membership_free.membership_type)

    def test_membership_model_price_decimal_field(self):
        obj = Membership.objects.get(id=1)
        decimal_price = obj._meta.get_field("price")
        self.assertEqual(decimal_price.max_digits, 5)
        self.assertEqual(decimal_price.decimal_places, 2)

    def test_membership_type_default_value(self):
        obj = Membership.objects.get(id=1)
        self.assertTrue(obj.membership_type, "Free")
