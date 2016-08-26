# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import os
from django.db import models
from django.utils.timezone import now as timezone_now
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible


def small_upload_to(instance, filename):
    now = timezone_now()
    filename_base, filename_ext = os.path.splitext(filename)
    return "locations/%s%s" % (
        now.strftime("%Y/%m/%Y%m%d%H%M%S_small"),
        filename_ext.lower(),
    )


def medium_upload_to(instance, filename):
    now = timezone_now()
    filename_base, filename_ext = os.path.splitext(filename)
    return "locations/%s%s" % (
        now.strftime("%Y/%m/%Y%m%d%H%M%S_medium"),
        filename_ext.lower(),
    )


def large_upload_to(instance, filename):
    now = timezone_now()
    filename_base, filename_ext = os.path.splitext(filename)
    return "locations/%s%s" % (
        now.strftime("%Y/%m/%Y%m%d%H%M%S_large"),
        filename_ext.lower(),
    )


@python_2_unicode_compatible
class Location(models.Model):
    title = models.CharField(_("Title"), max_length=255)
    slug = models.CharField(_("Slug"), max_length=255)

    latitude = models.FloatField(_("Latitude"), help_text=_("Latitude (Lat.) is the angle between any point and the equator (north pole is at 90; south pole is at -90)."), blank=True, null=True)
    longitude = models.FloatField(_("Longitude"), help_text=_("Longitude (Long.) is the angle east or west of an arbitrary point on Earth from Greenwich (UK), which is the international zero-longitude point (longitude=0 degrees). The anti-meridian of Greenwich is both 180 (direction to east) and -180 (direction to west)."), blank=True, null=True)

    small_image = models.ImageField(_("Small Image"), upload_to=small_upload_to)
    medium_image = models.ImageField(_("Medium Image"), upload_to=medium_upload_to)
    large_image = models.ImageField(_("Large Image"), upload_to=large_upload_to)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Location")
        verbose_name_plural = _("Locations")

