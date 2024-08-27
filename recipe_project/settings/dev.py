import environ

from .base import *

env = environ.Env(DEBUG=(bool, True))
environ.Env.read_env(str(BASE_DIR / ".env"))

SECRET_KEY = env.str("SECRET_KEY")
DEBUG = env.bool("DEBUG")

ALLOWED_HOSTS = ["*"]


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
