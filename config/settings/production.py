import os
import dj_database_url
from .base import *

environ.Env.read_env(os.path.join(BASE_DIR, ".env.production"))
SECRET_KEY = env("SECRET_KEY_PRODUCTION")

DEBUG = False

ALLOWED_HOSTS = []


# Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

DATABASES = {
    "default": dj_database_url.config(
        default=env("DB_URL"),
        conn_max_age=600,
    )
}

if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
