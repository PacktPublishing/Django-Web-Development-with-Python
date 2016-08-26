# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ViralVideo


@receiver(post_save, sender=ViralVideo)
def inform_administrators(sender, **kwargs):
    from django.core.mail import mail_admins
    instance = kwargs["instance"]
    created = kwargs["created"]
    if created:
        context = {
            "title": instance.title,
            "link": instance.get_url(),
        }
        plain_text_message = """
A new viral video called "%(title)s" has been created.
You can preview it at %(link)s.""" % context
        html_message = """
<p>A new viral video called "%(title)s" has been created.</p>
<p>You can preview it <a href="%(link)s">here</a>.</p>""" % context

        mail_admins(
            subject="New Viral Video Added at example.com",
            message=plain_text_message,
            html_message=html_message,
            fail_silently=True,
        )