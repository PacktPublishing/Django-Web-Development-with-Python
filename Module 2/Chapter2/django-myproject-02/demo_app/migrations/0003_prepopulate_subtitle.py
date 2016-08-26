# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def prepopulate_subtitle(apps, schema_editor):
    from django.conf import settings
    Idea = apps.get_model('demo_app', 'Idea')
    for idea in Idea.objects.all():
        for lang_code, lang_name in settings.LANGUAGES:
            setattr(idea, 'subtitle_%s' % lang_code, 'Dummy subtitle')
        idea.save()


class Migration(migrations.Migration):

    dependencies = [
        ('demo_app', '0002_subtitle_added'),
    ]

    operations = [
        migrations.RunPython(prepopulate_subtitle),
    ]
