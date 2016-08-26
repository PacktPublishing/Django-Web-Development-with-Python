# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.conf.urls import patterns, url

urlpatterns = patterns("cv.views",
    url(r'^(?P<cv_id>\d+)/pdf/$', "download_cv_pdf", name="download_cv_pdf"),
)