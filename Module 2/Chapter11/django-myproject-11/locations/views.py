# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404

from .models import Location


def location_list(request):
    location_list = Location.objects.all()
    return render(request, "locations/location_list.html", {"location_list": location_list})


def location_detail(request, slug):
    location = get_object_or_404(Location, slug=slug)
    return render(request, "locations/location_detail.html", {"location": location})


def location_detail_popup(request, slug):
    location = get_object_or_404(Location, slug=slug)
    return render(request, "locations/location_detail_popup.html", {"location": location})