# -*- coding: UTF-8 -*-
"""
Django settings for myproject project.
"""
from __future__ import unicode_literals
import os

gettext = lambda s: s

PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

SECRET_KEY = "nsxm!+-#cq5h0)lf1d+4=@6f(tq+)nr3t3^f^swoj$wc1_47sz"

DEBUG = True

ALLOWED_HOSTS = []

MEDIA_ROOT = os.path.join(PROJECT_PATH, "myproject", "media")

STATIC_ROOT = os.path.join(PROJECT_PATH, "myproject", "static")

STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, "myproject", "site_static"),
)

LOCALE_PATHS = (
    os.path.join(PROJECT_PATH, "locale"),
)

FILE_UPLOAD_TEMP_DIR = os.path.join(PROJECT_PATH, "myproject", "tmp")

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": (
            os.path.join(PROJECT_PATH, "myproject", "templates"),
        ),
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": (
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.template.context_processors.csrf",
                "django.template.context_processors.request",
                "django.contrib.messages.context_processors.messages",
                "sekizai.context_processors.sekizai",
                "cms.context_processors.cms_settings",
            ),
            "debug": True,
        },
    },
]

INSTALLED_APPS = (
    "djangocms_admin_style",
    "djangocms_text_ckeditor",

    # contributed
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",

    # third party
    "cms",
    "treebeard",
    "menus",
    "sekizai",
    
    "djangocms_file",
    "djangocms_flash",
    "djangocms_googlemap",
    "djangocms_inherit",
    "djangocms_picture",
    "djangocms_teaser",
    "djangocms_video",
    "djangocms_link",
    "djangocms_snippet",
    "reversion",

    # project-specific
    "movies",
    "editorial",
    "cms_extensions",
    "utils",
)

MIDDLEWARE_CLASSES = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "cms.middleware.user.CurrentUserMiddleware",
    "cms.middleware.page.CurrentPageMiddleware",
    "cms.middleware.toolbar.ToolbarMiddleware",
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

CMS_LANGUAGES = {
    "default": {
        "public": True,
        "hide_untranslated": False,
        "redirect_on_fallback": True,
    },
    1: [
        {
            "public": True,
            "code": "en",
            "hide_untranslated": False,
            "name": gettext("en"),
            "redirect_on_fallback": True,
        },
        {
            "public": True,
            "code": "de",
            "hide_untranslated": False,
            "name": gettext("de"),
            "redirect_on_fallback": True,
        },
        {
            "public": True,
            "code": "fr",
            "hide_untranslated": False,
            "name": gettext("fr"),
            "redirect_on_fallback": True,
        },
        {
            "public": True,
            "code": "lt",
            "hide_untranslated": False,
            "name": gettext("lt"),
            "redirect_on_fallback": True,
        },
    ],
}

TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

from utils.misc import get_git_changeset
STATIC_URL = "/static/%s/" % get_git_changeset(PROJECT_PATH)

MEDIA_URL = "/media/"

SITE_ID = 1

CMS_TEMPLATES = (
    ("cms/default.html", gettext("Default")),
    ("cms/start.html", gettext("Homepage")),
    ("cms/magazine.html", gettext("Magazine")),
)
CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {
    "main_content": {
        "name": gettext("Main Content"),
        "plugins": ("EditorialContentPlugin", "TextPlugin"),
    },
    "cms/magazine.html main_content": {
        "name": gettext("Magazine Main Content"),
        "plugins": ("EditorialContentPlugin", "TextPlugin"),
        "extra_context": {
            "editorial_content_template": "cms/plugins/editorial_content/magazine.html",
        }
    },
}

CMS_APPHOOKS = (
    "movies.cms_app.MoviesApphook",
)

MIGRATION_MODULES = {
    "cms": "cms.migrations",
    "menus": "menus.migrations",

    # Add also the following modules if you"re using these plugins:
    "djangocms_file": "djangocms_file.migrations_django",
    "djangocms_flash": "djangocms_flash.migrations_django",
    "djangocms_googlemap": "djangocms_googlemap.migrations_django",
    "djangocms_inherit": "djangocms_inherit.migrations_django",
    "djangocms_link": "djangocms_link.migrations_django",
    "djangocms_picture": "djangocms_picture.migrations_django",
    "djangocms_snippet": "djangocms_snippet.migrations_django",
    "djangocms_teaser": "djangocms_teaser.migrations_django",
    "djangocms_video": "djangocms_video.migrations_django",
    "djangocms_text_ckeditor": "djangocms_text_ckeditor.migrations",
}