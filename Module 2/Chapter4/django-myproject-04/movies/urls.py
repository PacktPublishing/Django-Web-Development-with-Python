# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.conf.urls import patterns, url

urlpatterns = patterns("movies.views",
    url(r"^$", "movie_list", name="movie_list"),
)