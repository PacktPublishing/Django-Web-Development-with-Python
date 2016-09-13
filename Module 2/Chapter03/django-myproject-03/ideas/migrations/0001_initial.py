# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title_en', models.CharField(max_length=200, verbose_name='Title (en)')),
                ('title_de', models.CharField(max_length=200, verbose_name='Title (de)', blank=True)),
                ('title_fr', models.CharField(max_length=200, verbose_name='Title (fr)', blank=True)),
                ('title_lt', models.CharField(max_length=200, verbose_name='Title (lt)', blank=True)),
            ],
            options={
                'verbose_name': 'Idea Category',
                'verbose_name_plural': 'Idea Categories',
            },
        ),
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_original', models.BooleanField(verbose_name='Original')),
                ('subtitle_en', models.CharField(max_length=200, verbose_name='Subtitle (en)', blank=True)),
                ('subtitle_de', models.CharField(max_length=200, verbose_name='Subtitle (de)', blank=True)),
                ('subtitle_fr', models.CharField(max_length=200, verbose_name='Subtitle (fr)', blank=True)),
                ('subtitle_lt', models.CharField(max_length=200, verbose_name='Subtitle (lt)', blank=True)),
                ('description_en', models.TextField(verbose_name='Description (en)', blank=True)),
                ('description_de', models.TextField(verbose_name='Description (de)', blank=True)),
                ('description_fr', models.TextField(verbose_name='Description (fr)', blank=True)),
                ('description_lt', models.TextField(verbose_name='Description (lt)', blank=True)),
                ('title_en', models.CharField(max_length=200, verbose_name='Title (en)')),
                ('title_de', models.CharField(max_length=200, verbose_name='Title (de)', blank=True)),
                ('title_fr', models.CharField(max_length=200, verbose_name='Title (fr)', blank=True)),
                ('title_lt', models.CharField(max_length=200, verbose_name='Title (lt)', blank=True)),
                ('categories', models.ManyToManyField(related_name='ideas', verbose_name='Categories', to='ideas.Category', blank=True)),
            ],
            options={
                'verbose_name': 'Idea',
                'verbose_name_plural': 'Ideas',
            },
        ),
    ]
