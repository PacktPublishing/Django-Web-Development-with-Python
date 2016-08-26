# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.conf.urls import patterns, url

urlpatterns = patterns("",
    url(r"^$", "movies.views.movie_list", name="movie_list"),
    url(r"^add/$", "movies.views.add_movie", name="add_movie"),
    url(r"^categories/$", "movies.views.movie_category_list", name="movie_list"),
)