import logging

from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse

from accounts.models import Subscription

from .membership_utility import get_selected_membership, get_user_membership


def update_transaction_view(request, subscription_id):
    user_membership = get_user_membership(request)
    selected_membership = get_selected_membership(request)
    user_membership.membership = selected_membership
    user_membership.save()
    sub, created = Subscription.objects.get_or_create(profile=user_membership)
    sub.stripe_subscription_id = subscription_id
    sub.active = True
    sub.save()
    try:
        del request.session["selected_membership_type"]
    except KeyError:
        logging.getLogger("error_logger").error(
            f'{request.session["selected_membership_type"]} not deleted'
        )
    messages.success(request, f"Successfull { selected_membership } created")
    return redirect(reverse("memberships:select"))
