# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='subtitle_de',
            field=models.CharField(max_length=200, verbose_name='Subtitle (de)', blank=True),
        ),
        migrations.AddField(
            model_name='idea',
            name='subtitle_en',
            field=models.CharField(max_length=200, verbose_name='Subtitle (en)', blank=True),
        ),
        migrations.AddField(
            model_name='idea',
            name='subtitle_fr',
            field=models.CharField(max_length=200, verbose_name='Subtitle (fr)', blank=True),
        ),
        migrations.AddField(
            model_name='idea',
            name='subtitle_lt',
            field=models.CharField(max_length=200, verbose_name='Subtitle (lt)', blank=True),
        ),
    ]
