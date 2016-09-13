# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import os
import requests
from StringIO import StringIO

from django.utils.six.moves import range
from django.core.management.base import BaseCommand
from django.utils.encoding import force_text
from django.conf import settings
from django.core.files import File

from music.models import Track


SILENT, NORMAL, VERBOSE, VERY_VERBOSE = 0, 1, 2, 3


class Command(BaseCommand):
    help = "Imports top tracks from last.fm as XML."

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            "--max_pages",
            type=int,
            default=0,
        )

    def handle(self, *args, **options):
        self.verbosity = options.get("verbosity", NORMAL)
        max_pages = options["max_pages"]

        params = {
            "method": "tag.gettoptracks",
            "tag": "disco",
            "api_key": settings.LAST_FM_API_KEY,
            "format": "json",
        }

        r = requests.get(
            "http://ws.audioscrobbler.com/2.0/",
            params=params
        )

        response_dict = r.json()
        total_pages = int(response_dict["tracks"]["@attr"]["totalPages"])
        if max_pages > 0:
            total_pages = max_pages

        if self.verbosity >= NORMAL:
            self.stdout.write("=== Tracks imported ===")

        self.save_page(response_dict)
        for page_number in range(2, total_pages + 1):
            params["page"] = page_number
            r = requests.get(
                "http://ws.audioscrobbler.com/2.0/",
                params=params
            )
            response_dict = r.json()
            self.save_page(response_dict)

    def save_page(self, d):
        for track_dict in d["tracks"]["track"]:
            track, created = Track.objects.get_or_create(
                name=force_text(track_dict["name"]),
                artist=force_text(track_dict["artist"]["name"]),
                url=force_text(track_dict["url"]),
            )
            image_dict = track_dict.get("image", None)
            if created and image_dict:
                image_url = image_dict[1]["#text"]
                image_response = requests.get(image_url)
                track.image.save(
                    os.path.basename(image_url),
                    File(StringIO(image_response.content))
                )
            if self.verbosity >= NORMAL:
                self.stdout.write(" - {} - {}".format(
                    track.artist, track.name
                ))
