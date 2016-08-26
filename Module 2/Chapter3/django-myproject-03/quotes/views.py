# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import os
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import FileResponse
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required

from .models import InspirationalQuote
from .forms import InspirationalQuoteForm


def add_quote(request):
    if request.method == "POST":
        form = InspirationalQuoteForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            quote = form.save()
            return redirect("add_quote_done")
    else:
        form = InspirationalQuoteForm()
    return render(request, "quotes/change_quote.html", {"form": form})


@login_required(login_url="my_login_page")
def download_quote_picture(request, quote_id):
    quote = get_object_or_404(InspirationalQuote, pk=quote_id)
    file_name, file_extension = os.path.splitext(quote.picture.file.name)
    file_extension = file_extension[1:]  # remove the dot
    response = FileResponse(quote.picture.file, content_type="image/%s" % file_extension)
    response['Content-Disposition'] = "attachment; filename=%s---%s.%s" % (
        slugify(quote.author)[:100],
        slugify(quote.quote)[:100],
        file_extension
    )
    return response