# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.utils.html import mark_safe
from mptt.forms import TreeNodeChoiceField

from crispy_forms.helper import FormHelper
from crispy_forms import layout, bootstrap

from utils.fields import MultipleChoiceTreeField
from .models import Movie, Category


class MovieFilterForm(forms.Form):
    category = TreeNodeChoiceField(
        label=_("Category"),
        queryset=Category.objects.all(),
        required=False,
        level_indicator=mark_safe("&nbsp;&nbsp;&nbsp;&nbsp;"),
    )

    def __init__(self, *args, **kwargs):
        super(MovieFilterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False


class MovieForm(forms.ModelForm):
    categories = MultipleChoiceTreeField(
        label=_("Categories"),
        required=False,
        queryset=Category.objects.all(),
    )

    class Meta:
        model = Movie

    def __init__(self, *args, **kwargs):
        super(MovieForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_action = ""
        self.helper.form_method = "POST"

        self.helper.layout = layout.Layout(
            layout.Field("title"),
            layout.Field("categories", template="utils/checkbox_select_multiple_tree.html"),
            bootstrap.FormActions(
                layout.Submit("submit", _("Save")),
            )
        )



