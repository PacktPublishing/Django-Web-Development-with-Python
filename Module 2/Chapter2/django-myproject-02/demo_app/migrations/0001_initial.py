# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
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
                ('created', models.DateTimeField(verbose_name='creation date and time', editable=False)),
                ('modified', models.DateTimeField(verbose_name='modification date and time', null=True, editable=False)),
                ('meta_keywords', models.CharField(help_text='Separate keywords by comma.', max_length=255, verbose_name='Keywords', blank=True)),
                ('meta_description', models.CharField(max_length=255, verbose_name='Description', blank=True)),
                ('meta_author', models.CharField(max_length=255, verbose_name='Author', blank=True)),
                ('meta_copyright', models.CharField(max_length=255, verbose_name='Copyright', blank=True)),
                ('is_original', models.BooleanField(verbose_name='Original')),
                ('description_en', models.TextField(verbose_name='Description (en)', blank=True)),
                ('description_de', models.TextField(verbose_name='Description (de)', blank=True)),
                ('description_fr', models.TextField(verbose_name='Description (fr)', blank=True)),
                ('description_lt', models.TextField(verbose_name='Description (lt)', blank=True)),
                ('title_en', models.CharField(max_length=200, verbose_name='Title (en)')),
                ('title_de', models.CharField(max_length=200, verbose_name='Title (de)', blank=True)),
                ('title_fr', models.CharField(max_length=200, verbose_name='Title (fr)', blank=True)),
                ('title_lt', models.CharField(max_length=200, verbose_name='Title (lt)', blank=True)),
                ('category', models.ForeignKey(verbose_name='Category', blank=True, to='demo_app.Category', null=True)),
            ],
            options={
                'verbose_name': 'Idea',
                'verbose_name_plural': 'Ideas',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(verbose_name='creation date and time', editable=False)),
                ('modified', models.DateTimeField(verbose_name='modification date and time', null=True, editable=False)),
                ('object_id', models.CharField(default=b'', help_text='Please enter the ID of the related object.', max_length=255, verbose_name='Related object')),
                ('owner_object_id', models.CharField(default=b'', help_text='Please enter the ID of the related object.', max_length=255, verbose_name='Owner')),
                ('content_type', models.ForeignKey(verbose_name="Related object's type (model)", to='contenttypes.ContentType', help_text='Please select the type (model) for the relation, you want to build.')),
                ('owner_content_type', models.ForeignKey(related_name='owner', verbose_name="Owner's type (model)", to='contenttypes.ContentType', help_text='Please select the type (model) for the relation, you want to build.')),
            ],
            options={
                'verbose_name': 'Like',
                'verbose_name_plural': 'Likes',
            },
        ),
    ]
