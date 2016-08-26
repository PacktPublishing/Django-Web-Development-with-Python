# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import datetime
from django.shortcuts import render, get_object_or_404
from django.db import models
from django.views.decorators.vary import vary_on_cookie  # use for Caching recipe
from django.views.decorators.cache import cache_page  # use for Caching recipe
from django.conf import settings
from .models import ViralVideo

POPULAR_FROM = getattr(settings, "VIRAL_VIDEOS_POPULAR_FROM", 500)

@vary_on_cookie
@cache_page(60)
def viral_video_detail(request, id):
    yesterday = datetime.date.today() - datetime.timedelta(days=1)

    qs = ViralVideo.objects.annotate(
        total_impressions=models.F("desktop_impressions") + models.F("mobile_impressions"),
        label=models.Case(
            models.When(total_impressions__gt=POPULAR_FROM, then=models.Value("popular")),
            models.When(created__gt=yesterday, then=models.Value("new")),
            default=models.Value("cool"),
            output_field=models.CharField(),
        ),
    )

    # DEBUG: check the SQL query that Django ORM generates
    print(qs.query)

    qs = qs.filter(pk=id)
    if request.flavour == "mobile":
        qs.update(mobile_impressions=models.F("mobile_impressions") + 1)
    else:
        qs.update(desktop_impressions=models.F("desktop_impressions") + 1)

    video = get_object_or_404(qs)

    return render(request, "viral_videos/viral_video_detail.html", {'video': video})