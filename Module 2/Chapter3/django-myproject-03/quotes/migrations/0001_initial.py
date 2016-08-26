# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import quotes.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InspirationalQuote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=200, verbose_name='Author')),
                ('quote', models.TextField(verbose_name='Quote')),
                ('picture', models.ImageField(upload_to=quotes.models.upload_to, null=True, verbose_name='Picture', blank=True)),
            ],
            options={
                'verbose_name': 'Inspirational Quote',
                'verbose_name_plural': 'Inspirational Quotes',
            },
        ),
    ]
