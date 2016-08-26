#!/home/myproject/bin/python
# -*- coding: utf-8 -*-
import os, sys, site
django_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__),
    '../lib/python2.6/site-packages/'),
)
site.addsitedir(django_path)
project_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__),
    '../project/myproject'),
)
sys.path += [project_path]
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()