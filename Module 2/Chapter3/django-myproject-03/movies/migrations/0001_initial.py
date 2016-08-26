# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=40, verbose_name='First name')),
                ('last_name', models.CharField(max_length=40, verbose_name='Last name')),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=40, verbose_name='First name')),
                ('last_name', models.CharField(max_length=40, verbose_name='Last name')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('rating', models.PositiveIntegerField(choices=[(1, '\u2606'), (2, '\u2606\u2606'), (3, '\u2606\u2606\u2606'), (4, '\u2606\u2606\u2606\u2606'), (5, '\u2606\u2606\u2606\u2606\u2606')])),
                ('actors', models.ManyToManyField(to='movies.Actor', blank=True)),
                ('directors', models.ManyToManyField(to='movies.Director', blank=True)),
                ('genres', models.ManyToManyField(to='movies.Genre', blank=True)),
            ],
        ),
    ]
