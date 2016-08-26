# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

from bulletin_board.views import RESTBulletinList, RESTBulletinDetail

urlpatterns = patterns("",
    url(r"^bulletin-board/", include("bulletin_board.urls")),
    url(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    url(r"^admin/", include(admin.site.urls)),

    url(r"^rest-api/bulletin-board/$", RESTBulletinList.as_view(), name="rest_bulletin_list"),
    url(r"^rest-api/bulletin-board/(?P<pk>[0-9]+)/$", RESTBulletinDetail.as_view(), name="rest_bulletin_detail"),

    url(r"^locations/", include("locations.urls")),
    url(r"^likes/", include("likes.urls")),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
