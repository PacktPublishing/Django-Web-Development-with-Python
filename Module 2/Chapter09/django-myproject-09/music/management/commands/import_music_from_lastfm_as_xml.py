# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import os
import requests
from xml.etree import ElementTree
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
            "format": "xml",
        }

        r = requests.get(
            "http://ws.audioscrobbler.com/2.0/",
            params=params
        )

        root = ElementTree.fromstring(r.content)
        total_pages = int(root.find("tracks").attrib["totalPages"])
        if max_pages > 0:
            total_pages = max_pages

        if self.verbosity >= NORMAL:
            self.stdout.write("=== Tracks imported ===")

        self.save_page(root)
        for page_number in range(2, total_pages + 1):
            params["page"] = page_number
            r = requests.get(
                "http://ws.audioscrobbler.com/2.0/",
                params=params
            )
            root = ElementTree.fromstring(r.content)
            self.save_page(root)

    def save_page(self, root):
        for track_node in root.findall("tracks/track"):
            track, created = Track.objects.get_or_create(
                name=force_text(track_node.find("name").text),
                artist=force_text(track_node.find("artist/name").text),
                url=force_text(track_node.find("url").text),
            )
            image_node = track_node.find("image[@size='medium']")
            if created and image_node is not None:
                image_response = requests.get(image_node.text)
                track.image.save(
                    os.path.basename(image_node.text),
                    File(StringIO(image_response.content))
                )
            if self.verbosity >= NORMAL:
                self.stdout.write(" - {} - {}".format(
                    track.artist, track.name
                ))
