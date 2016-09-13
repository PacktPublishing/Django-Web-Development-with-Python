# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.admin import User, Group
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType


class UserAdminExtended(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "is_active", "is_staff", "date_joined", "last_login")
    list_filter = ("is_active", "is_staff", "is_superuser", "date_joined", "last_login")
    ordering = ("last_name", "first_name", "username")
    save_on_top = True


class GroupAdminExtended(GroupAdmin):
    list_display = ("__unicode__", "display_users")
    save_on_top = True

    def display_users(self, obj):
        links = []
        for user in obj.user_set.all():
            ct = ContentType.objects.get_for_model(user)
            url = reverse(
                "admin:{}_{}_change".format(
                    ct.app_label, ct.model
                ),
                args=(user.id,)
            )
            links.append(
                """<a href="{}" target="_blank">{}</a>""".format(
                    url,
                    "{} {}".format(
                        user.first_name, user.last_name
                    ).strip() or user.username,
                )
            )
        return u"<br />".join(links)
    display_users.allow_tags = True
    display_users.short_description = _("Users")
    
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, UserAdminExtended)
admin.site.register(Group, GroupAdminExtended)
