# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.conf.urls import *

from .feeds import BulletinFeed

urlpatterns = patterns("bulletin_board.views",
    url(r"^$", "bulletin_list", name="bulletin_list"),
    url(r"^rss/$", BulletinFeed(), name="bulletin_rss"),
)