# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def copy_categories(apps, schema_editor):
    Idea = apps.get_model('demo_app', 'Idea')
    for idea in Idea.objects.all():
        if idea.category:
            idea.categories.add(idea.category)


class Migration(migrations.Migration):

    dependencies = [
        ('demo_app', '0004_categories_added'),
    ]

    operations = [
        migrations.RunPython(copy_categories),
    ]
