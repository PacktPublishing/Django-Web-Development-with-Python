# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible


COUNTRY_CHOICES = (
    ("UK", _("United Kingdom")),
    ("DE", _("Germany")),
    ("FR", _("France")),
    ("LT", _("Lithuania")),
)


@python_2_unicode_compatible
class Location(models.Model):
    title = models.CharField(_("title"), max_length=255, unique=True)
    description = models.TextField(_("description"), blank=True)
    street_address = models.CharField(_("street address"), max_length=255, blank=True)
    street_address2 = models.CharField(_("street address (2nd line)"), max_length=255, blank=True)
    postal_code = models.CharField(_("postal code"), max_length=10, blank=True)
    city = models.CharField(_("city"), max_length=255, blank=True)
    country = models.CharField(_("country"), max_length=2, blank=True, choices=COUNTRY_CHOICES)
    latitude = models.FloatField(_("latitude"), help_text=_("Latitude (Lat.) is the angle between any point and the equator (north pole is at 90; south pole is at -90)."), blank=True, null=True)
    longitude = models.FloatField(_("longitude"), help_text=_("Longitude (Long.) is the angle east or west of an arbitrary point on Earth from Greenwich (UK), which is the international zero-longitude point (longitude=0 degrees). The anti-meridian of Greenwich is both 180 (direction to east) and -180 (direction to west)."), blank=True, null=True)

    class Meta:
        verbose_name = _("Location")
        verbose_name_plural = _("Locations")

    def __str__(self):
        return self.title