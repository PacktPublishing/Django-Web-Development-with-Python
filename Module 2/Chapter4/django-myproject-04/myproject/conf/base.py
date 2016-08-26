# -*- coding: UTF-8 -*-
"""
Django settings for myproject project.
"""

from __future__ import unicode_literals
import os

PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

SECRET_KEY = "nsxm!+-#cq5h0)lf1d+4=@6f(tq+)nr3t3^f^swoj$wc1_47sz"

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

MEDIA_ROOT = os.path.join(PROJECT_PATH, "myproject", "media")

STATIC_ROOT = os.path.join(PROJECT_PATH, "myproject", "static")

STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, "myproject", "site_static"),
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, "myproject", "templates"),
)

LOCALE_PATHS = (
    os.path.join(PROJECT_PATH, "locale"),
)

FILE_UPLOAD_TEMP_DIR = os.path.join(PROJECT_PATH, "myproject", "tmp")

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)

INSTALLED_APPS = (
    # contributed
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # third party
    "crispy_forms",
    "ajaxuploader",

    # project-specific
    "locations",
    "utils",
    "likes",
    "quotes",
)

MIDDLEWARE_CLASSES = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
)

ROOT_URLCONF = "myproject.urls"

WSGI_APPLICATION = "myproject.wsgi.application"

LANGUAGE_CODE = "en"

LANGUAGES = (
    ("en", "English"),
    ("de", "Deutsch"),
    ("fr", "Français"),
    ("lt", "Lietuvių"),
)

TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

from utils.misc import get_git_changeset
STATIC_URL = "/static/%s/" % get_git_changeset(PROJECT_PATH)

MEDIA_URL = "/media/"

CRISPY_TEMPLATE_PACK = "bootstrap3"
