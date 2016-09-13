# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(verbose_name='creation date and time', editable=False)),
                ('modified', models.DateTimeField(verbose_name='modification date and time', null=True, editable=False)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('url', models.URLField(verbose_name='URL', blank=True)),
                ('release_year', models.PositiveIntegerField(verbose_name='Release Year')),
            ],
            options={
                'verbose_name': 'Movie',
                'verbose_name_plural': 'Movies',
            },
        ),
    ]
