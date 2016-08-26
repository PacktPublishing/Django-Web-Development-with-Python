# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inspirationalquote',
            name='language',
            field=models.CharField(blank=True, max_length=2, verbose_name='Language', choices=[('en', 'English'), ('de', 'Deutsch'), ('fr', 'Fran\xe7ais'), ('lt', 'Lietuvi\u0173')]),
        ),
    ]
