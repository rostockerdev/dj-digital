import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "loggers": {
        "": {"level": "DEBUG", "handlers": ["console"]},
        "info_logger": {"level": "INFO", "handlers": ["info_file"], "propagate": False},
        "error_logger": {
            "level": "WARNING",
            "handlers": ["error_file", "mail_admins"],
            "propagate": False,
        },
    },
    "formatters": {
        "info-formatter": {
            "format": "%(levelname)s : %(message)s at %(asctime)s  [ in %(pathname)s  %(funcName)s  %(lineno)d ]"
        },
        "error-formatter": {
            "format": "%(levelname)s : %(message)s at %(asctime)s [ in %(process)d  %(pathname)s  %(funcName)s  %(lineno)d ]"
        },
        "tiny": {"format": "%(levelname)s : %(message)s %(asctime)s"},
    },
    "handlers": {
        "console": {
            "level": "WARNING",
            "class": "logging.StreamHandler",
            "formatter": "tiny",
        },
        "info_file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": os.path.join(BASE_DIR, "Logger/logs/InfoLoggers.log"),
            "formatter": "info-formatter",
        },
        "error_file": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "filename": os.path.join(BASE_DIR, "Logger/logs/ErrorLoggers.log"),
            "formatter": "error-formatter",
        },
        "mail_admins": {
            "level": "ERROR",
            "class": "django.utils.log.AdminEmailHandler",
        },
    },
}
