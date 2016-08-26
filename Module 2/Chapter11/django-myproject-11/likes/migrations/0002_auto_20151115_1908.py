# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='object_id',
            field=models.CharField(default='', help_text='Please enter the ID of the related object.', max_length=255, verbose_name='Related object'),
        ),
    ]
