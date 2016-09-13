# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django import forms
from django.utils.translation import ugettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms import layout, bootstrap

from .models import Category, TYPE_CHOICES


class BulletinFilterForm(forms.Form):
    bulletin_type = forms.ChoiceField(
        label=_("Bulletin Type"),
        required=False,
        choices=(("", "---------"),) + TYPE_CHOICES,
    )
    category = forms.ModelChoiceField(
        label=_("Category"),
        required=False,
        queryset=Category.objects.all(),
    )

    def __init__(self, *args, **kwargs):
        super(BulletinFilterForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_action = ""
        self.helper.form_method = "GET"

        self.helper.layout = layout.Layout(
            layout.Fieldset(
                _("Filter bulletins"),
                layout.Field("bulletin_type"),
                layout.Field("category"),
            ),
            bootstrap.FormActions(
                layout.Submit("submit", _("Filter")),
            ),
        )