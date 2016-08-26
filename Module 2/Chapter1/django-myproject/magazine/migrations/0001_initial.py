# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('content', models.TextField(verbose_name='Content')),
                ('status', models.CharField(max_length=20, verbose_name='Status', choices=[('imported', 'Imported'), ('draft', 'Draft'), ('published', 'Published'), ('not_listed', 'Not Listed'), ('expired', 'Expired')])),
            ],
            options={
                'verbose_name': 'News Article',
                'verbose_name_plural': 'News Articles',
            },
        ),
    ]
