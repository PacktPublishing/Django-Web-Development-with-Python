# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import json
from django.http import HttpResponse
from django.views.decorators.cache import never_cache
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy

from .models import Like
from .templatetags.likes_tags import get_likes_count


@never_cache
@csrf_exempt
def json_set_like(request, content_type_id, object_id):
    """
    Sets the object as a favorite for the current user
    """
    json_str = "false"
    if request.user.is_authenticated() and request.method == "POST":
        content_type = ContentType.objects.get(id=content_type_id)
        obj = content_type.get_object_for_this_type(pk=object_id)
        like, is_created = Like.objects.get_or_create(
            content_type=ContentType.objects.get_for_model(obj),
            object_id=obj.pk,
            user=request.user,
        )
        if not is_created:
            like.delete()
        result = {
            "obj": unicode(obj),
            "action": is_created and "added" or "removed",
            "count": get_likes_count(obj),
        }
        json_str = json.dumps(result, ensure_ascii=False, encoding="utf8")
    return HttpResponse(json_str, content_type="text/javascript; charset=utf-8")


@login_required(login_url=reverse_lazy("admin:login"))
def liked_object_list(request):
    likes = Like.objects.filter(user=request.user)
    return render(request, "likes/liked_object_list.html", {"object_list": likes})