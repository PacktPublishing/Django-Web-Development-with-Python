# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bulletin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(verbose_name='creation date and time', editable=False)),
                ('modified', models.DateTimeField(verbose_name='modification date and time', null=True, editable=False)),
                ('bulletin_type', models.CharField(max_length=20, verbose_name='Type', choices=[('searching', 'Searching'), ('offering', 'Offering')])),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(max_length=300, verbose_name='Description')),
                ('contact_person', models.CharField(max_length=255, verbose_name='Contact person')),
                ('phone', models.CharField(max_length=50, verbose_name='Phone', blank=True)),
                ('email', models.CharField(max_length=254, verbose_name='Email', blank=True)),
                ('image', models.ImageField(upload_to='bulletin_board/', max_length=255, verbose_name='Image', blank=True)),
            ],
            options={
                'ordering': ('-created',),
                'verbose_name': 'Bulletin',
                'verbose_name_plural': 'Bulletins',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AddField(
            model_name='bulletin',
            name='category',
            field=models.ForeignKey(verbose_name='Category', to='bulletin_board.Category'),
        ),
    ]
