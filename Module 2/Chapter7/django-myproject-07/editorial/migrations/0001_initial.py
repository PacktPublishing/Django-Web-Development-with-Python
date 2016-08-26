# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import editorial.models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_auto_20150607_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='EditorialContent',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('subtitle', models.CharField(max_length=255, verbose_name='Subtitle', blank=True)),
                ('description', models.TextField(verbose_name='Description', blank=True)),
                ('website', models.CharField(max_length=255, verbose_name='Website', blank=True)),
                ('image', models.ImageField(upload_to=editorial.models.upload_to, max_length=255, verbose_name='Image', blank=True)),
                ('image_caption', models.TextField(verbose_name='Image Caption', blank=True)),
                ('css_class', models.CharField(max_length=255, verbose_name='CSS Class', blank=True)),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': 'Editorial content',
                'verbose_name_plural': 'Editorial contents',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
