# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import locations.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.CharField(max_length=255, verbose_name='Slug')),
                ('latitude', models.FloatField(help_text='Latitude (Lat.) is the angle between any point and the equator (north pole is at 90; south pole is at -90).', null=True, verbose_name='Latitude', blank=True)),
                ('longitude', models.FloatField(help_text='Longitude (Long.) is the angle east or west of an arbitrary point on Earth from Greenwich (UK), which is the international zero-longitude point (longitude=0 degrees). The anti-meridian of Greenwich is both 180 (direction to east) and -180 (direction to west).', null=True, verbose_name='Longitude', blank=True)),
                ('small_image', models.ImageField(upload_to=locations.models.small_upload_to, verbose_name='Small Image')),
                ('medium_image', models.ImageField(upload_to=locations.models.medium_upload_to, verbose_name='Medium Image')),
                ('large_image', models.ImageField(upload_to=locations.models.large_upload_to, verbose_name='Large Image')),
            ],
            options={
                'verbose_name': 'Location',
                'verbose_name_plural': 'Locations',
            },
        ),
    ]
