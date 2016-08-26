# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.conf.urls import patterns, url

urlpatterns = patterns("",
    url(r"^add/$", "quotes.views.add_quote", name="add_quote"),
    url(r"^add/done/$", "django.shortcuts.render", {"template_name": "quotes/add_quote_done.html"}, name="add_quote_done"),
    url(r"^ajax-upload/$", "quotes.views.ajax_uploader", name="ajax_uploader"),
)