import os

from django.utils.translation import ugettext_lazy as _

from .base import BASE_DIR

####################################
##       LANGUAGE  CONFIGURATION  ##
####################################


LANGUAGE_CODE = "en"
# LANGUAGE_CODE = 'de'

LANGUAGES = (
    ("en", _("EN")),
    ("de", _("DE")),
)
LOCALE_PATHS = [os.path.join(BASE_DIR, "locale")]
