# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.timezone import now as timezone_now
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.core.exceptions import FieldError


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
        verbose_name=(prefix_verbose and _("%s's type (model)") % prefix_verbose or _("Related object's type (model)")),
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
