from decouple import config

from core.settings.base import BASE_DIR, os

from .base import *

###########################################
#        SECRET CONFIGURATION             #
###########################################
SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", default=False, cast=bool)
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


####################################
##  MAILGUN CONFIGURATION ##
####################################

MAILGUN_API_KEY = config("MAILGUN_API_PUBLIC_KEY")
ENCRYPT_KEY = b"i_D8bT2mswqAleNqCAUqRfcxsii4dQRLJk8-E1W0oow="

####################################
##  HAYSTACK CONFIGURATION ##
####################################
WHOOSH_INDEX = os.path.join(BASE_DIR, "whoosh/")
HAYSTACK_CONNECTIONS = {
    "default": {
        "ENGINE": "haystack.backends.whoosh_backend.WhooshEngine",
        "PATH": WHOOSH_INDEX,
    },
}
HAYSTACK_SIGNAL_PROCESSOR = "haystack.signals.RealtimeSignalProcessor"

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

try:
    from .language_settings import *
except Exception:
    pass
