# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Category
from .models import Movie
from .forms import MovieFilterForm, MovieForm


def movie_list(request):
    qs = Movie.objects.order_by("title")
    
    form = MovieFilterForm(data=request.REQUEST)

    facets = {
        "selected": {},
        "categories": {
            "category": Category.objects.all(),
        },
    }

    if form.is_valid():
        category = form.cleaned_data["category"]
        if category:
            facets["selected"]["category"] = category
            qs = qs.filter(categories=category).distinct()

    paginator = Paginator(qs, 15)

    page_number = request.GET.get("page")
    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, show first page.
        page = paginator.page(1)
    except EmptyPage:
        # If page is out of range, show last existing page.
        page = paginator.page(paginator.num_pages)

    context = {
        "form": form,
        "facets": facets,
        "object_list": page,
    }
    return render(request, "movies/movie_list.html", context)


def add_movie(request):
    # dummy view for the movie form
    form = MovieForm()
    return render(request, "movies/add_movie.html", {"form": form})


def movie_category_list(request):
    context = {
        "categories": Category.objects.all(),
    }
    return render(request, "movies/movie_category_list.html", context)
