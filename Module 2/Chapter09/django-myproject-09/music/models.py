# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import os
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.utils.text import slugify
from django.utils.encoding import python_2_unicode_compatible


def upload_to(instance, filename):
    filename_base, filename_ext = os.path.splitext(filename)
    return "tracks/%s--%s%s" % (
        slugify(instance.artist),
        slugify(instance.name),
        filename_ext.lower(),
    )


@python_2_unicode_compatible
class Track(models.Model):
    name = models.CharField(_("Name"), max_length=250)
    artist = models.CharField(_("Artist"), max_length=250)
    url = models.URLField(_("URL"))
    image = models.ImageField(_("Image"), upload_to=upload_to, blank=True, null=True)

    class Meta:
        verbose_name = _("Track")
        verbose_name_plural = _("Tracks")

    def __str__(self):
        return "%s - %s" % (self.artist, self.name)
