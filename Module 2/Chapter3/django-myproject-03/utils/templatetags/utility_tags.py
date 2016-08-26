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
    for key, value_list in context['request'].GET._iterlists():
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
    query_string = context['request'].path
    if len(query_params):
        query_string += "?%s" % urllib.urlencode([
            (key, force_str(value)) for (key, value) in query_params if value
        ]).replace("&", "&amp;")
    return query_string


@register.simple_tag(takes_context=True)
def add_to_query(context, *params_to_remove, **params_to_add):
    """ Renders a link with modified current query parameters """
    query_params = []
    # go through current query params..
    for key, value_list in context['request'].GET._iterlists():
        if not key in params_to_remove:
            # don't add key-value pairs which already exist in the query
            if key in params_to_add and unicode(params_to_add[key]) in value_list:
                params_to_add.pop(key)
            for value in value_list:
                query_params.append((key, value))
    # add the rest key-value pairs
    for key, value in params_to_add.items():
        query_params.append((key, value))
    # empty values will be removed
    query_string = context['request'].path
    if len(query_params):
        query_string += "?%s" % urllib.urlencode([
            (key, force_str(value)) for (key, value) in query_params if value
        ]).replace("&", "&amp;")
    return query_string


@register.simple_tag(takes_context=True)
def remove_from_query(context, *args, **kwargs):
    """ Renders a link with modified current query parameters """
    query_params = []
    # go through current query params..
    for key, value_list in context['request'].GET._iterlists():
        # skip keys mentioned in the args
        if not key in args:
            for value in value_list:
                # skip key-value pairs mentioned in kwargs
                if not (key in kwargs and unicode(value) == unicode(kwargs[key])):
                    query_params.append((key, value))
    # empty values will be removed
    query_string = context['request'].path
    if len(query_params):
        query_string = "?%s" % urllib.urlencode([
            (key, force_str(value)) for (key, value) in query_params if value
        ]).replace("&", "&amp;")
    return query_string