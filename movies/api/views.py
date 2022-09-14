
from rest_framework import viewsets

from movies.models import Genre, Movie, MovieNight

from movies.api.serializers import GenreSerializer, MovieSerializer, MovieNightSerializer



class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class MovieNightViewSet(viewsets.ModelViewSet):
    queryset = MovieNight.objects.all()
    serializer_class = MovieNightSerializer