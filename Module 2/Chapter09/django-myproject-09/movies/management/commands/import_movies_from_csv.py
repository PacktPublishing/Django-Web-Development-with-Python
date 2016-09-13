# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import csv

from django.core.management.base import BaseCommand

from movies.models import Movie

SILENT, NORMAL, VERBOSE, VERY_VERBOSE = 0, 1, 2, 3


class Command(BaseCommand):
    help = (
        "Imports movies from a local CSV file. "
        "Expects title, URL, and release year."
    )

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument(
            "file_path",
            nargs=1,
            type=unicode,
        )

    def handle(self, *args, **options):
        verbosity = options.get("verbosity", NORMAL)
        file_path = options["file_path"][0]

        if verbosity >= NORMAL:
            self.stdout.write("=== Movies imported ===")

        with open(file_path) as f:
            reader = csv.reader(f)
            for rownum, (title, url, release_year) in enumerate(reader):
                if rownum == 0:
                    # let's skip the column captions
                    continue
                movie, created = Movie.objects.get_or_create(
                    title=title,
                    url=url,
                    release_year=release_year,
                )
                if verbosity >= NORMAL:
                    self.stdout.write("{}. {}".format(
                        rownum, movie.title
                    ))