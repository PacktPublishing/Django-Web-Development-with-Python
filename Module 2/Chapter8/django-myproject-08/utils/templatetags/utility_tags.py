# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import urllib
from django import template
from django.utils.encoding import force_str

register = template.Library()

@register.simple_tag(takes_context=True)
def modify_query(context, *params_to_remove, **params_to_change):
    """ Renders a link with modified current query parameters """
    query_params = []
    for key, value_list in context["request"].GET._iterlists():
        if not key in params_to_remove:
            # don't add key-value pairs for params to change
            if key in params_to_change:
                query_params.append((key, params_to_change[key]))
                params_to_change.pop(key)
            else:
                # leave existing parameters as they were if not mentioned in the params_to_change
                for value in value_list:
                    query_params.append((key, value))
    # attach new params
    for key, value in params_to_change.items():
        query_params.append((key, value))
    query_string = context["request"].path
    if len(query_params):
        query_string += "?%s" % urllib.urlencode([
            (key, force_str(value)) for (key, value) in query_params if value
        ]).replace("&", "&amp;")
    return query_string
