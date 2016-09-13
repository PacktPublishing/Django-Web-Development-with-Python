# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

from tastypie.api import Api
from bulletin_board.api import CategoryResource, BulletinResource

v1_api = Api(api_name="v1")
v1_api.register(CategoryResource())
v1_api.register(BulletinResource())

from bulletin_board.views import RESTBulletinList, RESTBulletinDetail

urlpatterns = patterns("",
    url(r"^bulletin-board/", include("bulletin_board.urls")),
    url(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    url(r"^admin/", include(admin.site.urls)),

    url(r"^rest-api/bulletin-board/$", RESTBulletinList.as_view(), name="rest_bulletin_list"),
    url(r"^rest-api/bulletin-board/(?P<pk>[0-9]+)/$", RESTBulletinDetail.as_view(), name="rest_bulletin_detail"),

    url(r"^api/", include(v1_api.urls)),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
