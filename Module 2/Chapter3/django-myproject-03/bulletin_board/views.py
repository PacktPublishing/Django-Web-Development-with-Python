# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

from .forms import BulletinForm


def add_bulletin(request):
    """
        Dummy view to show the form with layout
    """
    form = BulletinForm()
    return render(request, "bulletin_board/change_bulletin.html", {'form': form})
