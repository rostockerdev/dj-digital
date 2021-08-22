import os
from pathlib import Path

from django.contrib.messages import constants as messages

###########################################
#          BASE CONFIGURATION             #
###########################################
BASE_DIR = Path(__file__).resolve().parent.parent.parent


###########################################
#     APPLICATION CONFIGURATION           #
###########################################
LOCAL_APPS = [
    "pages.apps.PagesConfig",
    "errors.apps.ErrorsConfig",
    "accounts.apps.AccountsConfig",
    "memberships.apps.MembershipsConfig",
    "instructors.apps.InstructorsConfig",
]

THIRDPARTY_APPS = [
    "crispy_forms",
    "imagekit",
    "django.contrib.humanize",
    "django.contrib.sitemaps",
]


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Local App
    *LOCAL_APPS,
    # Third Party App
    *THIRDPARTY_APPS,
]

###########################################
#     MIDDLEWARE CONFIGURATION            #
###########################################

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

###########################################
#       TEMPLATE CONFIGURATION            #
###########################################

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


###########################################
#        PASSWORD CONFIGURATION           #
###########################################

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


###########################################
#        INTERNATIONALIZATION             #
###########################################

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


###########################################
#      STATIC FILE CONFIGURATION          #
###########################################

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = [os.path.join(BASE_DIR, "assets")]

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

####################################
##  LOGIN CONFIGURATION ##
####################################

# LOGIN_REDIRECT_URL = 'memberships:dashboard'
# LOGIN_URL = 'login'
CRISPY_TEMPLATE_PACK = "bootstrap4"


SITE_ID = 1
###########################################
#        MESSAGE  CONFIGURATION           #
###########################################

MESSAGE_TAGS = {messages.ERROR: "danger"}
