# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models import ViralVideo


class ViralVideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'modified', 'desktop_impressions', 'mobile_impressions')


admin.site.register(ViralVideo, ViralVideoAdmin)