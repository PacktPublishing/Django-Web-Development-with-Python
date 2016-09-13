# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import View

from .models import Genre
from .models import Director
from .models import Actor
from .models import Movie, RATING_CHOICES
from .forms import MovieFilterForm


def movie_list(request):
    paginate_by = 15
    qs = Movie.objects.order_by("title")
    
    form = MovieFilterForm(data=request.GET)

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
            rating = int(rating)
            facets["selected"]["rating"] = (rating, dict(RATING_CHOICES)[rating])
            qs = qs.filter(rating=rating).distinct()

    paginator = Paginator(qs, paginate_by)

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


class MovieListView(View):
    form_class = MovieFilterForm
    template_name = "movies/movie_list.html"
    paginate_by = 15

    def get(self, request, *args, **kwargs):
        form = self.form_class(data=request.GET)
        qs, facets = self.get_queryset_and_facets(form)
        page = self.get_page(request, qs)
        context = {
            "form": form,
            "facets": facets,
            "object_list": page,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def get_queryset_and_facets(self, form):
        qs = Movie.objects.order_by("title")

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
                rating = int(rating)
                facets["selected"]["rating"] = (rating, dict(RATING_CHOICES)[rating])
                qs = qs.filter(rating=rating).distinct()
        return qs, facets

    def get_page(self, request, qs):
        paginator = Paginator(qs, self.paginate_by)

        page_number = request.GET.get("page")
        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            # If page is not an integer, show first page.
            page = paginator.page(1)
        except EmptyPage:
            # If page is out of range, show last existing page.
            page = paginator.page(paginator.num_pages)
        return page
