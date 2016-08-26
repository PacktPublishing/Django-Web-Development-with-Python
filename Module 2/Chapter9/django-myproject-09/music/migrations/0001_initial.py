# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import music.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
                ('artist', models.CharField(max_length=250, verbose_name='Artist')),
                ('url', models.URLField(verbose_name='URL')),
                ('image', models.ImageField(upload_to=music.models.upload_to, null=True, verbose_name='Image', blank=True)),
            ],
            options={
                'verbose_name': 'Track',
                'verbose_name_plural': 'Tracks',
            },
        ),
    ]
