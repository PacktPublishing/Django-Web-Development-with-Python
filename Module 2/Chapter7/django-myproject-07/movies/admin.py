# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from models import Director, Actor, Genre, Movie

admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Movie)