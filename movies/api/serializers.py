from rest_framework import serializers

from movies.models import Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"

class MovieSerilaixer(serializers.ModelSerializer):
    genres = None
    pass