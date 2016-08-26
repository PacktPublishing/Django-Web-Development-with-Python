# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.i18n import i18n_patterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = i18n_patterns("",
    url(r"^$", "example.views.start_page", name="start_page"),
    url(r"^js-settings/$", "utils.views.render_js", {"template_name": "settings.js"}, name="js_settings"),

    #url(r"^likes/", include("likes.urls")),
    url(r"^admin/", include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
