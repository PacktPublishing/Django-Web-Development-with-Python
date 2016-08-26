# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework import generics

from .models import Bulletin
from .forms import BulletinFilterForm
from .serializers import BulletinSerializer


def bulletin_list(request):
    bulletins = Bulletin.objects.all()
    form = BulletinFilterForm(request.REQUEST)
    if form.is_valid():
        if form.cleaned_data["bulletin_type"]:
            bulletins = bulletins.filter(bulletin_type=form.cleaned_data["bulletin_type"])
        if form.cleaned_data["category"]:
            bulletins = bulletins.filter(category=form.cleaned_data["category"])

    return render(request, "bulletin_board/bulletin_list.html", {
        "form": form,
        "object_list": bulletins,
    })


class RESTBulletinList(generics.ListCreateAPIView):
    queryset = Bulletin.objects.all()
    serializer_class = BulletinSerializer


class RESTBulletinDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bulletin.objects.all()
    serializer_class = BulletinSerializer