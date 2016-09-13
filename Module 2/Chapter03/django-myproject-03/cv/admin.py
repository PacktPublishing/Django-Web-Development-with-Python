# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models import CV, Experience


class ExperienceInline(admin.StackedInline):
    model = Experience
    extra = 0


class CVAdmin(admin.ModelAdmin):
    inlines = [ExperienceInline]


admin.site.register(CV, CVAdmin)
