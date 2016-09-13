# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Genre
from .models import Director
from .models import Actor
from .models import Movie, RATING_CHOICES
from .forms import MovieFilterForm


def movie_list(request, featured=None, commercial=None, independent=None):
    qs = Movie.objects.order_by("title")
    if featured is not None:
        qs = qs.filter(featured=featured)
    if commercial is not None:
        qs = qs.filter(commercial=commercial)
    if independent is not None:
        qs = qs.filter(independent=independent)

    form = MovieFilterForm(data=request.REQUEST)

    facets = {
        "selected": {},
        "categories": {
            "genres": Genre.objects.all(),
            "directors": Director.objects.all(),
            "actors": Actor.objects.all(),
            "ratings": RATING_CHOICES,
        },
    }

    if form.is_valid():
        genre = form.cleaned_data["genre"]
        if genre:
            facets["selected"]["genre"] = genre
            qs = qs.filter(genres=genre).distinct()

        director = form.cleaned_data["director"]
        if director:
            facets["selected"]["director"] = director
            qs = qs.filter(directors=director).distinct()

        actor = form.cleaned_data["actor"]
        if actor:
            facets["selected"]["actor"] = actor
            qs = qs.filter(actors=actor).distinct()

        rating = form.cleaned_data["rating"]
        if rating:
            facets["selected"]["rating"] = (int(rating), dict(RATING_CHOICES)[int(rating)])
            qs = qs.filter(rating=rating).distinct()

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


def movie_detail(request, slug):
    movie = get_object_or_404(Movie, slug=slug)
    return render(request, "movies/movie_detail.html", {"object": movie})