# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.shortcuts import redirect
from django.shortcuts import render

from ajaxuploader.views import AjaxFileUploader

from .forms import InspirationQuoteForm


def add_quote(request):
    if request.method == "POST":
        form = InspirationQuoteForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            quote = form.save()
            return redirect("add_quote_done")
    else:
        form = InspirationQuoteForm()
    return render(request, "quotes/change_quote.html", {"form": form})


ajax_uploader = AjaxFileUploader()