import logging
import traceback

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http.response import BadHeaderError
from django.shortcuts import redirect
from django.template.loader import get_template
from django.urls import reverse
from django.utils.html import strip_tags

import requests


def send_email(data):
    try:
        url = "https://api.mailgun.net/v3/sandboxa1ce4b0a8f0a4f67b646321afa99a5a3.mailgun.org/messages"
        status = requests.post(
            url,
            auth=("api", settings.MAILGUN_API_KEY),
            data={
                "from": "Md. Mostofa kamal",
                "to": [data["email"]],
                "subject": data["subject"],
                "text": "sended test"
                # "text": data["plain_text"],
                # "html": data["html_text"],
            },
        )
        print(f"Status: {status}")
        # Email Send
        # m_subject = data["subject"]
        # m_body = data["html_text"]
        # f_mail = "rostockerdev@gmail.com"
        # t_mail = [data["email"]]
        # if m_subject and m_body and f_mail:
        #     try:
        #         send_mail(m_subject, m_body, f_mail, t_mail, fail_silently=False)
        #         # messages.success(
        #         #     request,
        #         #     "Your request has been submitted, a realtor will get back to you soon.",
        #         # )
        #         status = True
        #         logging.getLogger("info_logger").info(
        #             "Mail sent to " + data["email"] + ". status: " + str(status)
        #         )
        #     except BadHeaderError:
        #         # messages.error(request, "Invalid header was set.")
        #         logging.getLogger("error_logger").error(
        #             "Sorry, Was not possible to send the mail"
        #         )
        #         return redirect("home")
        logging.getLogger("info_logger").info(
            "Mail sent to " + data["email"] + ". status: " + str(status)
        )
        return True
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
