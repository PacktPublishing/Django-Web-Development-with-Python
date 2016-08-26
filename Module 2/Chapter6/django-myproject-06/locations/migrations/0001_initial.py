# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=255, verbose_name='title')),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('street_address', models.CharField(max_length=255, verbose_name='street address', blank=True)),
                ('street_address2', models.CharField(max_length=255, verbose_name='street address (2nd line)', blank=True)),
                ('postal_code', models.CharField(max_length=10, verbose_name='postal code', blank=True)),
                ('city', models.CharField(max_length=255, verbose_name='city', blank=True)),
                ('country', models.CharField(blank=True, max_length=2, verbose_name='country', choices=[(b'UK', 'United Kingdom'), (b'DE', 'Germany'), (b'FR', 'France'), (b'LT', 'Lithuania')])),
                ('latitude', models.FloatField(help_text='Latitude (Lat.) is the angle between any point and the equator (north pole is at 90; south pole is at -90).', null=True, verbose_name='latitude', blank=True)),
                ('longitude', models.FloatField(help_text='Longitude (Long.) is the angle east or west of an arbitrary point on Earth from Greenwich (UK), which is the international zero-longitude point (longitude=0 degrees). The anti-meridian of Greenwich is both 180 (direction to east) and -180 (direction to west).', null=True, verbose_name='longitude', blank=True)),
            ],
            options={
                'verbose_name': 'Location',
                'verbose_name_plural': 'Locations',
            },
        ),
    ]
