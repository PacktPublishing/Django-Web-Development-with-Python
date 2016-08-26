# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

### See recipe "Over-writable app settings"
# TO DO:
# 1) Run local server
# 2) Go to http://127.0.0.1:8000/admin/magazine/newsarticle/add/
# 3) Login with username "admin" and password "admin"
# 4) Note that the status choices are overwritten

from .app_settings import STATUS_CHOICES

test = "ąžuoliūkštis - some unicode literals to test"

@python_2_unicode_compatible
class NewsArticle(models.Model):
    title = models.CharField(_("Title"), max_length=200)
    content = models.TextField(_("Content"))
    status = models.CharField(_("Status"), max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("News Article")
        verbose_name_plural = _("News Articles")