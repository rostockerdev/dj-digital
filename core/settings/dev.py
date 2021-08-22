from decouple import config

from core.settings.base import BASE_DIR

from .base import *

###########################################
#        SECRET CONFIGURATION             #
###########################################
SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", default=True, cast=bool)
DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

###########################################
#        DATABASE CONFIGURATION           #
###########################################
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

###########################################
#          WSGI CONFIGURATION             #
###########################################
WSGI_APPLICATION = "core.wsgi.application"


####################################
##  STRIPE CONFIGURATION ##
####################################

STRIPE_PUBLIC_KEY = config("STRIPE_PUBLIC_KEY")
STRIPE_SECRET_KEY = config("STRIPE_SECRET_KEY")

###########################################
#           LOGGING CONFIGURATION         #
###########################################
try:
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

    from .log_settings import *

    sentry_sdk.init(
        dsn=config("SENTRY_DSN"),
        integrations=[DjangoIntegration()],
        traces_sample_rate=1.0,
        send_default_pii=True,
    )
except Exception:
    pass
