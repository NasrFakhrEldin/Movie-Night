
from rest_framework import viewsets

from movies.models import Genre

from movies.api.serializers import GenreSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer