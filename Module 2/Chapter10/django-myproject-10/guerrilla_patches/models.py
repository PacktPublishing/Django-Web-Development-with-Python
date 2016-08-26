# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.utils import text
from slugify import slugify_de as awesome_slugify

awesome_slugify.to_lower = True

text.slugify = awesome_slugify