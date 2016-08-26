# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.conf.urls import patterns, url

urlpatterns = patterns("likes.views",
    url(r"^$", "liked_object_list", name="liked_object_list"),
    url(r"^(?P<content_type_id>[^/]+)/(?P<object_id>[^/]+)/$", "json_set_like", name="json_set_like"),
)