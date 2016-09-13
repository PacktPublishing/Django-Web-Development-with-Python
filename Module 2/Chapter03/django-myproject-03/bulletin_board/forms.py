# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django import forms
from django.utils.translation import ugettext_lazy as _, ugettext

from crispy_forms.helper import FormHelper
from crispy_forms import layout, bootstrap

from .models import Bulletin


class BulletinForm(forms.ModelForm):
    class Meta:
        model = Bulletin
        fields = ["bulletin_type", "title", "description", "contact_person", "phone", "email", "image"]

    def __init__(self, *args, **kwargs):
        super(BulletinForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_action = ""
        self.helper.form_method = "POST"

        self.fields["bulletin_type"].widget = forms.RadioSelect()
        # delete empty choice for the type
        del self.fields["bulletin_type"].choices[0]

        self.helper.layout = layout.Layout(
            layout.Fieldset(
                _("Main data"),
                layout.Field("bulletin_type"),
                layout.Field("title", css_class="input-block-level"),
                layout.Field("description", css_class="input-block-level", rows="3"),
            ),
            layout.Fieldset(
                _("Image"),
                layout.Field("image", css_class="input-block-level"),
                layout.HTML(u"""{% load i18n %}
                    <p class="help-block">{% trans "Available formats are JPG, GIF, and PNG. Minimal size is 800 × 800 px." %}</p>
                """),
                title=_("Image upload"),
                css_id="image_fieldset",
            ),
            layout.Fieldset(
                _("Contact"),
                layout.Field("contact_person", css_class="input-block-level"),
                layout.Div(
                    bootstrap.PrependedText("phone", """<span class="glyphicon glyphicon-earphone"></span>""", css_class="input-block-level"),
                    bootstrap.PrependedText("email", "@", css_class="input-block-level", placeholder="contact@example.com"),
                    css_id="contact_info",
                ),
            ),
            bootstrap.FormActions(
                layout.Submit("submit", _("Save")),
            )
        )
