# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import re
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

from utils.models import CreationModificationDateMixin, UrlMixin


@python_2_unicode_compatible
class ViralVideo(CreationModificationDateMixin, UrlMixin):
    title = models.CharField(_("Title"), max_length=200, blank=True)
    embed_code = models.TextField(_("YouTube embed code"), blank=True)

    desktop_impressions = models.PositiveIntegerField(_("Desktop impressions"), default=0)
    mobile_impressions = models.PositiveIntegerField(_("Mobile impressions"), default=0)

    class Meta:
        verbose_name = _("Viral video")
        verbose_name_plural = _("Viral videos")

    def __str__(self):
        return self.title

    def get_url_path(self):
        from django.core.urlresolvers import reverse
        return reverse("viral_video_detail", kwargs={"id": str(self.id)})

    def get_thumbnail_url(self):
        if not hasattr(self, "_thumbnail_url_cached"):
            url_pattern = re.compile(r'src="https://www.youtube.com/embed/([^"]+)"')
            match = url_pattern.search(self.embed_code)
            self._thumbnail_url_cached = ""
            if match:
                video_id = match.groups()[0]
                self._thumbnail_url_cached = "http://img.youtube.com/vi/{}/0.jpg".format(video_id)
        return self._thumbnail_url_cached
