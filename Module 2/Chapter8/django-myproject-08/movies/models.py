# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

from utils.models import CreationModificationDateMixin

from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey, TreeManyToManyField


@python_2_unicode_compatible
class Category(MPTTModel, CreationModificationDateMixin):
    parent = TreeForeignKey("self", blank=True, null=True)
    title = models.CharField(_("Title"), max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["tree_id", "lft"]
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


@python_2_unicode_compatible
class Movie(CreationModificationDateMixin):
    title = models.CharField(_("Title"), max_length=255)
    categories = TreeManyToManyField(Category, verbose_name=_("Categories"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Movie")
        verbose_name_plural = _("Movies")
