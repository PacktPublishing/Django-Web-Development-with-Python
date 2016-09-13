# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms


class MultipleChoiceTreeField(forms.ModelMultipleChoiceField):
    widget = forms.CheckboxSelectMultiple

    def label_from_instance(self, obj):
        return obj