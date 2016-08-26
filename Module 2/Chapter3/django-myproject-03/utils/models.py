# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import urlparse

from django.conf import settings
from django.utils.timezone import now as timezone_now
from django.utils.safestring import mark_safe
from django.template.defaultfilters import escape
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.core.exceptions import FieldError


### See recipe "Model mixin with URL-related methods"

class UrlMixin(models.Model):
    """
    A replacement for get_absolute_url()
    Models extending this mixin should have either get_url or get_url_path implemented.
    http://code.djangoproject.com/wiki/ReplacingGetAbsoluteUrl
    """
    class Meta:
        abstract = True

    def get_url(self):
        if hasattr(self.get_url_path, "dont_recurse"):
            raise NotImplementedError
        try:
            path = self.get_url_path()
        except NotImplementedError:
            raise
        website_url = getattr(settings, "DEFAULT_WEBSITE_URL", "http://127.0.0.1:8000")
        return website_url + path
    get_url.dont_recurse = True

    def get_url_path(self):
        if hasattr(self.get_url, "dont_recurse"):
            raise NotImplementedError
        try:
            url = self.get_url()
        except NotImplementedError:
            raise
        bits = urlparse.urlparse(url)
        return urlparse.urlunparse(("", "") + bits[2:])
    get_url_path.dont_recurse = True

    def get_absolute_url(self):
        return self.get_url_path()


### See recipe "Model mixin handling creation and modification dates"

class CreationModificationDateMixin(models.Model):
    """
    Abstract base class with a creation and modification date and time
    """

    created = models.DateTimeField(
        _("creation date and time"),
        editable=False,
    )

    modified = models.DateTimeField(
        _("modification date and time"),
        null=True,
        editable=False,
    )

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created = timezone_now()
        else:
            # To ensure that we have a creation data always, we add this one
            if not self.created:
                self.created = timezone_now()

            self.modified = timezone_now()

        super(CreationModificationDateMixin, self).save(*args, **kwargs)
    save.alters_data = True

    class Meta:
        abstract = True


### See recipe "Model mixin taking care of meta tags"

class MetaTagsMixin(models.Model):
    """
    Abstract base class for meta tags in the <head> section
    """
    meta_keywords = models.CharField(
        _("Keywords"),
        max_length=255,
        blank=True,
        help_text=_("Separate keywords by comma."),
    )
    meta_description = models.CharField(
        _("Description"),
        max_length=255,
        blank=True,
    )
    meta_author = models.CharField(
        _("Author"),
        max_length=255,
        blank=True,
    )
    meta_copyright = models.CharField(
        _("Copyright"),
        max_length=255,
        blank=True,
    )

    class Meta:
        abstract = True

    def get_meta_keywords(self):
        meta_tag = ""
        if self.meta_keywords:
            meta_tag = """<meta name="keywords" content="%s" />\n""" % escape(self.meta_keywords)
        return mark_safe(meta_tag)

    def get_meta_description(self):
        meta_tag = ""
        if self.meta_description:
            meta_tag = """<meta name="description" content="%s" />\n""" % escape(self.meta_description)
        return mark_safe(meta_tag)

    def get_meta_author(self):
        meta_tag = ""
        if self.meta_author:
            meta_tag = """<meta name="author" content="%s" />\n""" % escape(self.meta_author)
        return mark_safe(meta_tag)

    def get_meta_copyright(self):
        meta_tag = ""
        if self.meta_copyright:
            meta_tag = """<meta name="copyright" content="%s" />\n""" % escape(self.meta_copyright)
        return mark_safe(meta_tag)

    def get_meta_tags(self):
        return mark_safe("".join((
            self.get_meta_keywords(),
            self.get_meta_description(),
            self.get_meta_author(),
            self.get_meta_copyright(),
        )))


### See recipe "Model mixin handling generic relations"

def object_relation_mixin_factory(
        prefix=None,
        prefix_verbose=None,
        add_related_name=False,
        limit_content_type_choices_to={},
        limit_object_choices_to={},
        is_required=False,
    ):
    """
    returns a mixin class for generic foreign keys using
    "Content type - object Id" with dynamic field names.
    This function is just a class generator

    Parameters:
    prefix : a prefix, which is added in front of the fields
    prefix_verbose :    a verbose name of the prefix, used to
                        generate a title for the field column
                        of the content object in the Admin.
    add_related_name :  a boolean value indicating, that a
                        related name for the generated content
                        type foreign key should be added. This
                        value should be true, if you use more
                        than one ObjectRelationMixin in your model.

    The model fields are created like this:

    <<prefix>>_content_type :   Field name for the "content type"
    <<prefix>>_object_id :      Field name for the "object Id"
    <<prefix>>_content_object : Field name for the "content object"

    """
    if prefix:
        p = "%s_" % prefix
    else:
        p = ""

    content_type_field = "%scontent_type" % p
    object_id_field = "%sobject_id" % p
    content_object_field = "%scontent_object" % p

    class TheClass(models.Model):
        class Meta:
            abstract = True

    if add_related_name:
        if not prefix:
            raise FieldError("if add_related_name is set to True, a prefix must be given")
        related_name = prefix
    else:
        related_name = None

    content_type = models.ForeignKey(
        ContentType,
        verbose_name=(_("%s's type (model)") % prefix_verbose
            if prefix_verbose
            else _("Related object's type (model)")
        ),
        related_name=related_name,
        blank=not is_required,
        null=not is_required,
        help_text=_("Please select the type (model) for the relation, you want to build."),
        limit_choices_to=limit_content_type_choices_to,
    )

    object_id = models.CharField(
        (prefix_verbose or _("Related object")),
        blank=not is_required,
        null=False,
        help_text=_("Please enter the ID of the related object."),
        max_length=255,
        default="",  # for south migrations
    )
    object_id.limit_choices_to = limit_object_choices_to
    # can be retrieved by MyModel._meta.get_field("object_id").limit_choices_to
    content_object = GenericForeignKey(
        ct_field=content_type_field,
        fk_field=object_id_field,
    )

    TheClass.add_to_class(content_type_field, content_type)
    TheClass.add_to_class(object_id_field, object_id)
    TheClass.add_to_class(content_object_field, content_object)

    return TheClass
