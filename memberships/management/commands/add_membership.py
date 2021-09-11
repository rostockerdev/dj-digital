from django.core.management.base import BaseCommand

from memberships.models import Membership


class Command(BaseCommand):
    help = "Add membership types to the Database"

    def handle(self, *args, **options):
        stripe_plan_ids = [
            "price_1JX9bpJCJmztk3yXFOoHlfTh",
            "price_1JX9bpJCJmztk3yXVqXCRB7c",
            "price_1JX9bpJCJmztk3yXWsXx0V5q",
        ]
        membership_slugs = ["Free", "Professional", "Enterprise"]
        membership_plans = ["Free", "Professional", "Enterprise"]
        for _ in range(3):
            if _ == 0:
                Membership.objects.create(
                    slug=membership_slugs[_],
                    membership_type=membership_plans[_],
                    stripe_plan_id=stripe_plan_ids[_],
                    price="0.00",
                )
            elif _ == 1:
                Membership.objects.create(
                    slug=membership_slugs[_],
                    membership_type=membership_plans[_],
                    stripe_plan_id=stripe_plan_ids[_],
                    price="5.00",
                )
            elif _ == 2:
                Membership.objects.create(
                    slug=membership_slugs[_],
                    membership_type=membership_plans[_],
                    stripe_plan_id=stripe_plan_ids[_],
                    price="10.00",
                )
        print("Completed!!! Check your database.")
