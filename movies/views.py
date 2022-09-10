from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from movies.forms import SearchForm, MovieNightForm

from movies.omdb_integration import search_and_save, fill_movie_details
from movies.models import Movie

from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request, "movies/index.html")


@login_required
def movie_search(request):
    search_form = SearchForm(request.POST)

    if search_form.is_valid() and search_form.cleaned_data["term"]:
        term = search_form.cleaned_data["term"]
        search_and_save(term)

        movie_list = Movie.objects.filter(title__icontains=term)

        did_search = True
    else:
        movie_list= []
        did_search = False

    return render(request, "movies/search.html",{
        "page_group": "search",
        "search_form": search_form,
        "movie_list": movie_list,
        "did_search": did_search,
    })

@login_required
def movie_detail(request, imdb_id):
    movie = get_object_or_404(Movie, imdb_id=imdb_id)
    fill_movie_details(movie)

    if request.method == "POST":
        movie_night_form = MovieNightForm(request.POST)

        if movie_night_form.is_valid():
            movie_night = movie_night_form.save(False)
            movie_night.movie = movie
            movie_night.creator = request.user
            movie_night.save()

            return redirect("movie_night_detail_ui", movie_night.pk)
    else:
        movie_night_form = MovieNightForm()
        
    render(request, "movies/movie_detail.html", {
        "page_group": "search",
        "movie": movie,
        "movie_night_form": movie_night_form,
    })


def movie_night_detail(request):
    return HttpResponse("Test")