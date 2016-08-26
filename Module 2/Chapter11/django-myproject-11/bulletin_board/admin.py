# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Category, Bulletin

admin.site.register(Category)
admin.site.register(Bulletin)