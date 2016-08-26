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
    "django_mobile.context_processors.flavour",
)

TEMPLATE_LOADERS = (
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
    "django_mobile.loader.Loader",
)

INSTALLED_APPS = (
    "guerrilla_patches",

    # contributed
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # third party
    "debug_toolbar",
    "django_mobile",

    # project-specific
    "utils",
    "viral_videos",
)

MIDDLEWARE_CLASSES = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "utils.middleware.ThreadLocalMiddleware",
    "django_mobile.middleware.MobileDetectionMiddleware",
    "django_mobile.middleware.SetFlavourMiddleware",
)

ROOT_URLCONF = "myproject.urls"

WSGI_APPLICATION = "myproject.wsgi.application"

LANGUAGE_CODE = "en"

LANGUAGES = (
    ("en", u"English"),
    ("de", u"Deutsch"),
    ("fr", u"Français"),
    ("lt", u"Lietuvių"),
)

TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

from utils.misc import get_git_changeset
STATIC_URL = "/static/%s/" % get_git_changeset(PROJECT_PATH)

MEDIA_URL = "/media/"


### Debug Toolbar Settings ###

DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": [],
    "SHOW_TOOLBAR_CALLBACK": "utils.misc.custom_show_toolbar",
    "SHOW_TEMPLATE_CONTEXT": True,
}

DEBUG_TOOLBAR_PANELS = [
    "debug_toolbar.panels.versions.VersionsPanel",
    "debug_toolbar.panels.timer.TimerPanel",
    "debug_toolbar.panels.settings.SettingsPanel",
    "debug_toolbar.panels.headers.HeadersPanel",
    "debug_toolbar.panels.request.RequestPanel",
    "debug_toolbar.panels.sql.SQLPanel",
    "debug_toolbar.panels.templates.TemplatesPanel",
    "debug_toolbar.panels.staticfiles.StaticFilesPanel",
    "debug_toolbar.panels.cache.CachePanel",
    "debug_toolbar.panels.signals.SignalsPanel",
    "debug_toolbar.panels.logging.LoggingPanel",
    "debug_toolbar.panels.redirects.RedirectsPanel",
]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
        },
        "null": {
            "class": "django.utils.log.NullHandler",
        },
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
            "include_html": True,  # <-- the important part
        }
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
        },
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": False,
        },
        "django.security": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": False,
        },
        "py.warnings": {
            "handlers": ["console"],
        },
    }
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
        "LOCATION": "127.0.0.1:11211",
        "TIMEOUT": 60,  # 1 minute
        "KEY_PREFIX": "myproject_production",
    }
}

ADMINS = (
    #("Admin", "admin@example.com"),
)