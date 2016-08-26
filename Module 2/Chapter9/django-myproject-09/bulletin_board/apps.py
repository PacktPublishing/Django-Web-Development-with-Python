# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class BulletinBoardConfig(AppConfig):
    name = "bulletin_board"
    verbose_name = _("Bulletin Board")