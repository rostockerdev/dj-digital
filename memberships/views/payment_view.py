from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import View

import stripe

from .membership_utility import get_selected_membership, get_user_membership


class PaymentView(View):
    def get(self, *args, **kwargs):
        context = {"selected_membership": get_selected_membership(self.request)}
        return render(self.request, "memberships/membership_payment.html", context)

    def post(self, *args, **kwargs):
        token = self.request.POST.get("stripeToken")
        user_membership = get_user_membership(self.request)
        try:
            selected_membership = get_selected_membership(self.request)
        except Exception:
            return redirect("memberships:select")
        # amount = int(selected_membership.price)
        try:
            customer = stripe.Customer.retrieve(user_membership.stripe_customer_id)
            customer.source = token
            customer.save()

            """
            Now we can create the subscription using only the customer as we don't need to pass their
            credit card source anymore
            """
            subscription = stripe.Subscription.create(
                customer=user_membership.stripe_customer_id,
                items=[
                    {"plan": selected_membership.stripe_plan_id},
                ],
            )
            return redirect(
                reverse(
                    "memberships:update-transactions",
                    kwargs={"subscription_id": subscription.id},
                )
            )

        except stripe.error.CardError as e:
            body = e.json_body
            err = body.get("error", {})
            messages.warning(self.request, f"{err.get('message')}")
            return redirect("memberships:select")

        except stripe.error.RateLimitError as e:
            # Too many requests made to the API too quickly
            body = e.json_body
            err = body.get("error", {})
            messages.warning(self.request, f"{err.get('message')}")
            return redirect("memberships:select")

        except stripe.error.InvalidRequestError as e:
            # Invalid parameters were supplied to Stripe's API
            body = e.json_body
            err = body.get("error", {})
            messages.warning(self.request, f"{err.get('message')}")
            return redirect("memberships:select")

        except stripe.error.AuthenticationError as e:
            # Authentication with Stripe's API failed
            # (maybe you changed API keys recently)
            body = e.json_body
            err = body.get("error", {})
            messages.warning(self.request, f"{err.get('message')}")
            return redirect("memberships:select")

        except stripe.error.APIConnectionError as e:
            # Network communication with Stripe failed
            body = e.json_body
            err = body.get("error", {})
            messages.warning(self.request, f"{err.get('message')}")
            return redirect("memberships:select")

        except stripe.error.StripeError as e:
            # Display a very generic error to the user, and maybe send
            # yourself an email
            body = e.json_body
            err = body.get("error", {})
            messages.warning(self.request, f"{err.get('message')}")
            # messages.warning(
            #     self.request,
            #     "Something went wrong. You were not charged. Please try again.",
            # )
            return redirect("memberships:select")

        except Exception as e:
            # send an email to ourselves
            body = e.json_body
            err = body.get("error", {})
            messages.warning(self.request, f"{err.get('message')}")
            # messages.warning(
            #     self.request, "A serious error occurred. We have been notifed."
            # )
            return redirect("memberships:select")
