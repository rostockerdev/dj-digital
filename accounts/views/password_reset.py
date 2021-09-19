from django import template
from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import BadHeaderError, EmailMultiAlternatives, send_mail
from django.db.models.query_utils import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data["email"]
            associated_users = User.objects.filter(Q(email=data) | Q(username=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    plaintext = template.loader.get_template(
                        "accounts/password_reset_email.txt"
                    )
                    htmltemp = template.loader.get_template(
                        "accounts/password_reset_email.html"
                    )
                    c = {
                        "email": user.email,
                        "domain": "127.0.0.1:8000",
                        "site_name": "djdigitalhub",
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        "token": default_token_generator.make_token(user),
                        "protocol": "http",
                    }
                    text_content = plaintext.render(c)
                    html_content = htmltemp.render(c)
                    try:
                        msg = EmailMultiAlternatives(
                            subject,
                            text_content,
                            "Website <rostockerdev@gmail.com>",
                            [user.email],
                            headers={"Reply-To": "rostockerdev@gmail.com"},
                        )
                        msg.attach_alternative(html_content, "text/html")
                        msg.send()
                    except BadHeaderError:
                        return HttpResponse("Invalid header found.")
                    messages.info(
                        request,
                        "Password reset instructions have been sent to the email address entered.",
                    )
                    return redirect("password_reset_done")
    password_reset_form = PasswordResetForm()
    return render(
        request=request,
        template_name="accounts/password_reset.html",
        context={"password_reset_form": password_reset_form},
    )
