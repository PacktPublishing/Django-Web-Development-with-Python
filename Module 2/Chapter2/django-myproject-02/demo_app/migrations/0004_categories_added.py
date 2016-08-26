# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo_app', '0003_prepopulate_subtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='categories',
            field=models.ManyToManyField(related_name='ideas', verbose_name='Categories', to='demo_app.Category', blank=True),
        ),
    ]
