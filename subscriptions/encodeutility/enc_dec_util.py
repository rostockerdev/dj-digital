import base64
import logging
import traceback

from cryptography.fernet import Fernet
from django.conf import settings

# ENCRYPT_KEY = Fernet.generate_key()


def encrypt(txt):
    try:
        # first convert the integer or others to string
        txt = str(txt)
        # Get the Key fro the settings
        cipher_suite = Fernet(settings.ENCRYPT_KEY)
        # input should be byte, so convert the text to byte
        encrypted_text = cipher_suite.encrypt(txt.encode("ascii"))
        # the encode to urlsafe base64 formant
        encrypted_text = base64.urlsafe_b64encode(encrypted_text).decode("ascii")
        return encrypted_text
    except Exception:
        logging.getLogger("error_logger").error(traceback.format_exc())
        return None


def decrypt(txt):
    try:
        txt = base64.urlsafe_b64decode(txt)
        cipher_suite = Fernet(settings.ENCRYPT_KEY)
        decoded_text = cipher_suite.decrypt(txt).decode("ascii")
        return decoded_text
    except Exception:
        logging.getLogger("error_logger").error(traceback.format_exc())
        return None
