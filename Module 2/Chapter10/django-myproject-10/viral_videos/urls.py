# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.conf.urls import *

urlpatterns = [
    url(r'^(?P<id>\d+)/', "viral_videos.views.viral_video_detail", name="viral_video_detail"),
]