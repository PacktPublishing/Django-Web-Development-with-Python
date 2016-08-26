# -*- coding: UTF-8 -*-
import urllib
from django import template
from django.utils.encoding import force_str

register = template.Library()

@register.simple_tag(takes_context=True)
def append_to_query(context, no_path=False, **kwargs):
    query_params = context['request'].GET.copy()
    for key, value in kwargs.items():
        query_params[key] = value
    path = u""
    if len(query_params):
        path += u"?%s" % urllib.urlencode([
            (key, force_str(value)) for (key, value) in query_params.iteritems() if value
        ])
    return path