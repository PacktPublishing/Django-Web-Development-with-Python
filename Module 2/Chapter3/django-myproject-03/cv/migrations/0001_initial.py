# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=40, verbose_name='First name')),
                ('last_name', models.CharField(max_length=40, verbose_name='Last name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('from_date', models.DateField(verbose_name='From')),
                ('till_date', models.DateField(null=True, verbose_name='Till', blank=True)),
                ('company', models.CharField(max_length=100, verbose_name='Company')),
                ('position', models.CharField(max_length=100, verbose_name='Position')),
                ('skills', models.TextField(verbose_name='Skills gained', blank=True)),
                ('cv', models.ForeignKey(to='cv.CV')),
            ],
            options={
                'ordering': ('-from_date',),
            },
        ),
    ]
