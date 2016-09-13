# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.core.urlresolvers import NoReverseMatch
from django.utils.encoding import python_2_unicode_compatible

from utils.models import UrlMixin
from utils.models import CreationModificationDateMixin
from utils.models import MetaTagsMixin
from utils.models import object_relation_mixin_factory

from utils.fields import MultilingualCharField, MultilingualTextField


### See recipe "Changing foreign key to many-to-many field with South"

@python_2_unicode_compatible
class Category(models.Model):
    title = MultilingualCharField(_("Title"), max_length=200)

    class Meta:
        verbose_name = _("Idea Category")
        verbose_name_plural = _("Idea Categories")

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Idea(UrlMixin, CreationModificationDateMixin, MetaTagsMixin):
    title = MultilingualCharField(_("Title"), max_length=200)
    subtitle = MultilingualCharField(_("Subtitle"), max_length=200, blank=True)
    description = MultilingualTextField(_("Description"), blank=True)
    is_original = models.BooleanField(_("Original"))
    # category = models.ForeignKey(Category, verbose_name=_("Category"), null=True, blank=True)
    categories = models.ManyToManyField(Category, verbose_name=_("Categories"), blank=True, related_name="ideas")

    class Meta:
        verbose_name = _("Idea")
        verbose_name_plural = _("Ideas")

    def __str__(self):
        return self.title

    def get_url_path(self):
        try:
            return reverse("idea_detail", kwargs={"id": self.pk})
        except NoReverseMatch:
            return ""



### See recipe "Model mixin handling generic relations"

FavoriteObjectMixin = object_relation_mixin_factory(
    is_required=True,
)


OwnerMixin = object_relation_mixin_factory(
    prefix="owner",
    prefix_verbose=_("Owner"),
    add_related_name=True,
    limit_content_type_choices_to={"model__in": ("user", "institution")},
    is_required=True,
)


@python_2_unicode_compatible
class Like(FavoriteObjectMixin, OwnerMixin, CreationModificationDateMixin):

    class Meta:
        verbose_name = _("Like")
        verbose_name_plural = _("Likes")

    def __str__(self):
        return _("%(owner)s likes %(obj)s") % {
            "owner": self.owner_content_object,
            "obj": self.content_object,
        }