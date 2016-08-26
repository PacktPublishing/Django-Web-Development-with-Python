# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.utils.translation import get_language
from haystack import indexes
from ideas.models import Idea
from quotes.models import InspirationalQuote


class IdeaIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True)

    def get_model(self):
        return Idea

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

    def prepare_text(self, obj):
        # this will be called for each language / backend
        return "\n".join((
            obj.title,
            obj.subtitle,
            obj.description,
            '\n'.join([cat.title for cat in obj.categories.all()]),
        ))


class InspirationQuoteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True)

    def get_model(self):
        return InspirationalQuote

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        if using and using != "default":
            lang_code = using.replace("default_", "")
        else:
            lang_code = settings.LANGUAGE_CODE[:2]
        return self.get_model().objects.filter(language=lang_code)

    def prepare_text(self, obj):
        # this will be called for each language / backend
        return "\n".join((
            obj.author,
            obj.quote,
        ))