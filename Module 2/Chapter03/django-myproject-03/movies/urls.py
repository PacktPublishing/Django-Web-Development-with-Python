# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.conf.urls import patterns, url

from .views import MovieListView

urlpatterns = patterns('',
    url(r'^$', 'movies.views.movie_list', name="movie_list"),
    url(r'^alternative/$', MovieListView.as_view(), name="movie_list"),
)