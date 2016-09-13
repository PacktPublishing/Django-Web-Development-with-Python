# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
#from mptt_tree_editor.admin import TreeEditor
from django_mptt_admin.admin import DjangoMpttAdmin

from .models import Category, Movie


# class CategoryAdmin(TreeEditor):
#     list_display = ["indented_short_title", "actions_column", "created", "modified"]
#     list_filter = ["created"]


class CategoryAdmin(DjangoMpttAdmin):
    list_display = ["title", "created", "modified"]
    list_filter = ["created"]


class MovieAdmin(admin.ModelAdmin):
    filter_horizontal = ["categories"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Movie, MovieAdmin)
