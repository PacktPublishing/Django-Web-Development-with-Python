# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.utils.encoding import python_2_unicode_compatible

from utils.models import CreationModificationDateMixin
from utils.models import UrlMixin

TYPE_CHOICES = (
    ("searching", _("Searching")),
    ("offering", _("Offering")),
)


@python_2_unicode_compatible
class Category(models.Model):
    title = models.CharField(_("Title"), max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


@python_2_unicode_compatible
class Bulletin(CreationModificationDateMixin, UrlMixin):
    bulletin_type = models.CharField(_("Type"), max_length=20, choices=TYPE_CHOICES)
    category = models.ForeignKey(Category, verbose_name=_("Category"))

    title = models.CharField(_("Title"), max_length=255)
    description = models.TextField(_("Description"), max_length=300)

    contact_person = models.CharField(_("Contact person"), max_length=255)
    phone = models.CharField(_("Phone"), max_length=50, blank=True)
    email = models.CharField(_("Email"), max_length=254, blank=True)

    image = models.ImageField(_("Image"), max_length=255, upload_to="bulletin_board/", blank=True)

    class Meta:
        verbose_name = _("Bulletin")
        verbose_name_plural = _("Bulletins")
        ordering = ("-created",)

    def __str__(self):
        return self.title

    def get_url_path(self):
        try:
            path = reverse("bulletin_detail", kwargs={"pk": self.pk})
        except:
            # the apphook is not attached yet
            return ""
        else:
            return path