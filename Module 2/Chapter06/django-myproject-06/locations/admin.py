# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django.template.loader import render_to_string

from .models import Location


class LocationAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ("title", "street_address", "description")
    search_fields = ("title", "street_address", "description")

    def get_fieldsets(self, request, obj=None):
        map_html = render_to_string("admin/includes/map.html")
        fieldsets = [
            (_("Main Data"), {"fields": ("title", "description")}),
            (_("Address"), {"fields": ("street_address", "street_address2", "postal_code", "city", "country", "latitude", "longitude")}),
            (_("Map"), {"description": map_html, "fields": []}),
        ]
        return fieldsets

admin.site.register(Location, LocationAdmin)
