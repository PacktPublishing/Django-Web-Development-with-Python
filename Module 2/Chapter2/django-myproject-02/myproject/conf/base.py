# -*- coding: UTF-8 -*-
"""
Django settings for myproject project.
"""

from __future__ import unicode_literals
import os
import sys

PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

EXTERNAL_LIBS_PATH = os.path.join(PROJECT_PATH, "externals", "libs")
EXTERNAL_APPS_PATH = os.path.join(PROJECT_PATH, "externals", "apps")
sys.path = ["", EXTERNAL_LIBS_PATH, EXTERNAL_APPS_PATH] + sys.path

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

# Application definition

INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "demo_app",
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

TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGE_CODE = "en"

LANGUAGES = (
    ("en", "English"),
    ("de", "Deutsch"),
    ("fr", "Français"),
    ("lt", "Lietuvių"),
)

from utils.misc import get_git_changeset
STATIC_URL = "/static/%s/" % get_git_changeset(PROJECT_PATH)

MEDIA_URL = "/media/"
