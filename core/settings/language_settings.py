import os

from django.utils.translation import ugettext_lazy as _

from .base import BASE_DIR

####################################
##       LANGUAGE  CONFIGURATION  ##
####################################


LANGUAGES = (
    ("en", _("EN")),
    ("de", _("DE")),
)
LANGUAGE_CODE = "en-us"
# LANGUAGE_CODE = 'de'
LOCALE_PATHS = [os.path.join(BASE_DIR, "locale")]
