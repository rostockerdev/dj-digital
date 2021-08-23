import logging
import traceback

from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import redirect
from django.utils import timezone

from subscriptions.encodeutility.enc_dec_util import decrypt, encrypt
from subscriptions.models import Subscribe

SUBSCRIBE_STATUS = "subscribed"
SEPARATOR = "&"


def subscription_confirmation(request):
    if request.method == "POST":
        raise Http404

    token = request.GET.get("token", None)
    if not token:
        logging.getLogger("error_logger").warning("Invalid Link")
        messages.error(request, "Invalid Link")
        return redirect("memberships:dashboard")

    token = decrypt(token)
    if token:
        token = token.split(SEPARATOR)
        email = token[0]
        # initiate_time = token[1]
        try:
            subscribe_model_instance = Subscribe.objects.get(email=email)
            subscribe_model_instance.status = SUBSCRIBE_STATUS
            subscribe_model_instance.updated_date = timezone.now()
            subscribe_model_instance.save()
            messages.success(request, "Subscription Confirmed. Thank you.")
        except ObjectDoesNotExist:
            logging.getLogger("error_logger").warning(traceback.format_exc())
            messages.error(request, "Invalid Link")
    else:
        logging.getLogger("error_logger").warning("Invalid token")
        messages.error(request, "Invalid Link")
    return redirect("memberships:dashboard")
