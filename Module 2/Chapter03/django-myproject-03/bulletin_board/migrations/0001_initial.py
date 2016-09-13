# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bulletin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bulletin_type', models.CharField(max_length=20, verbose_name='Type', choices=[('searching', 'Searching'), ('offering', 'Offering')])),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(max_length=300, verbose_name='Description')),
                ('contact_person', models.CharField(max_length=255, verbose_name='Contact person')),
                ('phone', models.CharField(max_length=200, verbose_name='Phone', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='Email', blank=True)),
                ('image', models.ImageField(upload_to='bulletin_board/', max_length=255, verbose_name='Image', blank=True)),
            ],
            options={
                'ordering': ('title',),
                'verbose_name': 'Bulletin',
                'verbose_name_plural': 'Bulletins',
            },
        ),
    ]
