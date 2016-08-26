# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class DemoAppConfig(AppConfig):
    name = 'demo_app'
    verbose_name = _("Demo App")