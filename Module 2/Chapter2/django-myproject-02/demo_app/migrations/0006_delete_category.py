# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo_app', '0005_copy_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='idea',
            name='category',
        ),
    ]
