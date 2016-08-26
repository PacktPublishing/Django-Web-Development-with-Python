# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ViralVideo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(verbose_name='creation date and time', editable=False)),
                ('modified', models.DateTimeField(verbose_name='modification date and time', null=True, editable=False)),
                ('title', models.CharField(max_length=200, verbose_name='Title', blank=True)),
                ('embed_code', models.TextField(verbose_name='YouTube embed code', blank=True)),
                ('desktop_impressions', models.PositiveIntegerField(default=0, verbose_name='Desktop impressions')),
                ('mobile_impressions', models.PositiveIntegerField(default=0, verbose_name='Mobile impressions')),
            ],
            options={
                'verbose_name': 'Viral video',
                'verbose_name_plural': 'Viral videos',
            },
        ),
    ]
