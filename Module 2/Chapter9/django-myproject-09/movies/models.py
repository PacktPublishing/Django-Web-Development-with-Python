# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

from utils.models import CreationModificationDateMixin


@python_2_unicode_compatible
class Movie(CreationModificationDateMixin):
    title = models.CharField(_("Title"), max_length=255)
    url = models.URLField(_("URL"), blank=True)
    release_year = models.PositiveIntegerField(_("Release Year"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Movie")
        verbose_name_plural = _("Movies")
