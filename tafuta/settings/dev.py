# tafuta/settings/dev.py
from ._base import *

DEBUG = True

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

THUMBNAIL_DEBUG = True