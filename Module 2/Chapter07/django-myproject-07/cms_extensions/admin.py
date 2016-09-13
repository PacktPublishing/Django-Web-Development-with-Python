# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from cms.extensions import PageExtensionAdmin

from .models import CSSExtension


class CSSExtensionAdmin(PageExtensionAdmin):
    pass

admin.site.register(CSSExtension, CSSExtensionAdmin)