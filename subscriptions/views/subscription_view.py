import datetime
import logging
from time import time

from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render, reverse
from django.utils import timezone

from subscriptions.emailutility.email_utility import send_subscription_email
from subscriptions.encodeutility.enc_dec_util import decrypt, encrypt
from subscriptions.models import Subscribe
from subscriptions.validation_utility import validate_email

SUBSCRIBE_STATUS = "subscribed"
SEPARATOR = "&"


def save_email(email):
    try:
        subscribe_model_instance = Subscribe.objects.get(email=email)
    except ObjectDoesNotExist:
        subscribe_model_instance = Subscribe()
        subscribe_model_instance.email = email
        subscribe_model_instance.created_date = timezone.now()
    except Exception:
        return False

    subscribe_model_instance.status = SUBSCRIBE_STATUS
    subscribe_model_instance.updated_date = timezone.now()
    subscribe_model_instance.save()
    return True


def subscription_view(request):
    if request.method == "POST":
        post_data = request.POST.copy()
        email = post_data.get("email", None)
        error_msg = validate_email(email)
        if error_msg:
            messages.error(request, error_msg)
            return redirect("home")

        save_status = save_email(email)
        if save_status:
            token = encrypt(email + SEPARATOR + str(datetime.time()))
            subscription_confirmation_url = (
                request.build_absolute_uri(
                    reverse("subscriptions:subscription-confirmation")
                )
                + "?token="
                + token
            )
            status = send_subscription_email(email, subscription_confirmation_url)
            if not status:
                Subscribe.objects.get(email=email).delete()
                logging.getLogger("info_logger").info(
                    "Deleted the record from Subscribe table for "
                    + email
                    + " as email sending failed. status: "
                    + str(status)
                )
            else:
                msg = (
                    "Mail sent to email Id '"
                    + email
                    + "'. Please confirm your subscription by clicking on "
                    "confirmation link provided in email. "
                    "Please check your spam folder as well."
                )
                logging.getLogger("error_logger").error("Hi I am here")
                messages.success(request, msg)

        else:
            msg = "Some error occurred. Please try in some time. Meanwhile we are looking into it."
            messages.error(request, msg)
        return redirect("memberships:dashboard")
