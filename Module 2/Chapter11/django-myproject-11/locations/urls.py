# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.conf.urls import patterns, url

urlpatterns = patterns("locations.views",
    url(r"^$", "location_list", name="location_list"),
    url(r"^(?P<slug>[^/]+)/$", "location_detail", name="location_detail"),
    url(r"^(?P<slug>[^/]+)/popup/$", "location_detail_popup", name="location_detail_popup"),
)