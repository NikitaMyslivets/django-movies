from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Movie
from django.views.generic.base import View


class MoviesView(ListView):
    # Список фильмов
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = 'movies/movies.html'


class MovieDetailView(DetailView):
    # Полное описание фильма
    model = Movie
    slug_field = 'url'

