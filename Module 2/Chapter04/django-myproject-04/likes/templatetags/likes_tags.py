# -*- coding: UTF-8 -*-
from django import template
from django.contrib.contenttypes.models import ContentType
from django.template import loader

from likes.models import Like

register = template.Library()


### TAGS ###

@register.tag
def like_widget(parser, token):
    try:
        # split_contents() knows how not to split quoted strings.
        tag_name, for_str, obj = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires a following syntax: {%% %r for <object> %%}" % (token.contents[0], token.contents[0])
    return ObjectLikeWidget(obj)


class ObjectLikeWidget(template.Node):
    def __init__(self, obj):
        self.obj = obj

    def render(self, context):
        obj = template.resolve_variable(self.obj, context)
        ct = ContentType.objects.get_for_model(obj)

        is_liked_by_user = bool(Like.objects.filter(
            user=context["request"].user,
            content_type=ct,
            object_id=obj.pk,
        ))

        context.push()
        context["object"] = obj
        context["content_type_id"] = ct.pk
        context["is_liked_by_user"] = is_liked_by_user
        context["count"] = get_likes_count(obj)

        output = loader.render_to_string("likes/includes/like.html", context)
        context.pop()
        return output


### FILTERS ###

@register.filter
def get_likes_count(obj):
    ct = ContentType.objects.get_for_model(obj)
    return Like.objects.filter(
        content_type=ct,
        object_id=obj.pk,
    ).count()
