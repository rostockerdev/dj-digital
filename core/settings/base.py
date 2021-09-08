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
    "courses.apps.CoursesConfig",
    "subscriptions.apps.SubscriptionsConfig",
    "notifications.apps.NotificationsConfig",
    "quizes.apps.QuizesConfig",
    "search.apps.SearchConfig",
]

THIRDPARTY_APPS = [
    "crispy_forms",
    "haystack",
    "imagekit",
    "whoosh",
    "ckeditor",
    "ckeditor_uploader",
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
    "django.middleware.locale.LocaleMiddleware",
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
                "notifications.context_processors.notification_count",
            ],
            "libraries": {
                "staticfiles": "django.templatetags.static",
            },
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

# LANGUAGE_CODE = "en-us"
# LANGUAGE_CODE = "en"

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

LOGIN_REDIRECT_URL = "memberships:dashboard"
LOGIN_URL = "login"
CRISPY_TEMPLATE_PACK = "bootstrap4"


SITE_ID = 1
###########################################
#        MESSAGE  CONFIGURATION           #
###########################################

MESSAGE_TAGS = {messages.ERROR: "danger"}


####################################
##  CKEDITOR CONFIGURATION ##
####################################

CKEDITOR_UPLOAD_PATH = "ck_uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_CONFIGS = {
    "default": {
        "height": 300,
        "width": 300,
        "toolbar_rostockerlabs": [
            {
                "name": "document",
                "items": [
                    "Source",
                    "-",
                    "Save",
                    "NewPage",
                    "Preview",
                    "Print",
                    "-",
                    "Templates",
                ],
            },
            {
                "name": "clipboard",
                "items": [
                    "Cut",
                    "Copy",
                    "Paste",
                    "PasteText",
                    "PasteFromWord",
                    "-",
                    "Undo",
                    "Redo",
                ],
            },
            {"name": "editing", "items": ["Find", "Replace", "-", "SelectAll"]},
            {
                "name": "forms",
                "items": [
                    "Form",
                    "Checkbox",
                    "Radio",
                    "TextField",
                    "Textarea",
                    "Select",
                    "Button",
                    "ImageButton",
                    "HiddenField",
                ],
            },
            "/",
            {
                "name": "basicstyles",
                "items": [
                    "Bold",
                    "Italic",
                    "Underline",
                    "Strike",
                    "Subscript",
                    "Superscript",
                    "-",
                    "RemoveFormat",
                ],
            },
            {
                "name": "paragraph",
                "items": [
                    "NumberedList",
                    "BulletedList",
                    "-",
                    "Outdent",
                    "Indent",
                    "-",
                    "Blockquote",
                    "CreateDiv",
                    "-",
                    "JustifyLeft",
                    "JustifyCenter",
                    "JustifyRight",
                    "JustifyBlock",
                    "-",
                    "BidiLtr",
                    "BidiRtl",
                    "Language",
                ],
            },
            {"name": "links", "items": ["Link", "Unlink", "Anchor"]},
            {
                "name": "insert",
                "items": [
                    "Image",
                    "Flash",
                    "Table",
                    "HorizontalRule",
                    "Smiley",
                    "SpecialChar",
                    "PageBreak",
                    "Iframe",
                ],
            },
            "/",
            {"name": "styles", "items": ["Styles", "Format", "Font", "FontSize"]},
            {"name": "colors", "items": ["TextColor", "BGColor"]},
            {"name": "tools", "items": ["Maximize", "ShowBlocks"]},
            {"name": "about", "items": ["About"]},
            "/",  # put this to force next toolbar on new line
            {
                "name": "yourcustomtools",
                "items": [
                    # put the name of your editor.ui.addButton here
                    "Preview",
                    "Maximize",
                ],
            },
        ],
    },
}
