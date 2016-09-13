# -*- coding: UTF-8 -*-
from django.contrib import admin
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from .models import Category, Idea, Like


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', )
    fieldsets = (
        (_("Title"), {'fields': ['title_%s' % lang_code for lang_code, lang_name in settings.LANGUAGES]}),
    )


class IdeaAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created', 'modified', 'is_original')
    fieldsets = (
        (_("Title"), {'fields': ['title_%s' % lang_code for lang_code, lang_name in settings.LANGUAGES]}),
        (_("Subtitle"), {'fields': ['subtitle_%s' % lang_code for lang_code, lang_name in settings.LANGUAGES]}),
        (_("Description"), {'fields': ['description_%s' % lang_code for lang_code, lang_name in settings.LANGUAGES]}),
        (None, {'fields': ['categories', 'is_original']}),
        (_("Meta tags"), {'fields': ['meta_keywords', 'meta_description', 'meta_author', 'meta_copyright']}),
    )
    filter_horizontal = ['categories']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Idea, IdeaAdmin)
admin.site.register(Like)