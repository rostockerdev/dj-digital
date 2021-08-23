import logging
import traceback

import requests
from django.conf import settings
from django.template.loader import get_template
from django.urls import reverse
from django.utils.html import strip_tags


def send_email(data):
    try:
        url = "https://api.mailgun.net/v3/sandboxa5146f9e78554380b3ec3231d6aca1a8.mailgun.org"
        status = requests.post(
            url,
            auth=("api", settings.MAILGUN_API_KEY),
            data={
                "from": "Md. Mostofa kamal",
                "to": [data["email"]],
                "subject": data["subject"],
                "text": data["plain_text"],
                "html": data["html_text"],
            },
        )
        logging.getLogger("info_logger").info(
            "Mail sent to " + data["email"] + ". status: " + str(status)
        )
        return status
    except Exception:
        logging.getLogger("error_logger").error(traceback.format_exc())
        return False


def send_subscription_email(email, subscription_confirmation_url):
    data = dict()
    data["confirmation_url"] = subscription_confirmation_url
    data["subject"] = "Please confirm The Subscription"
    data["email"] = email
    template = get_template("subscriptions/subscription_email.html")
    data["html_text"] = template.render(data)
    data["plain_text"] = strip_tags(data["html_text"])
    return send_email(data)
