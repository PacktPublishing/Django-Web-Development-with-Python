# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'email_messages.views.message_to_user', name="message_to_user"),
    url(r'^done/$', 'django.shortcuts.render', {'template_name': "email_messages/message_to_user_done.html"}, name="message_to_user_done"),
)