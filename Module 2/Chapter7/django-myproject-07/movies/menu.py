# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from cms.menu_bases import CMSAttachMenu


class MoviesMenu(CMSAttachMenu):
    name = _("Movies Menu")

    def get_nodes(self, request):
        nodes = [
            NavigationNode(_("Editor's Picks"), reverse("featured_movie_list"), 1),
            NavigationNode(_("Commercial Movies"), reverse("commercial_movie_list"), 2),
            NavigationNode(_("Independent Movies"), reverse("independent_movie_list"), 3),
        ]
        return nodes

menu_pool.register_menu(MoviesMenu)
