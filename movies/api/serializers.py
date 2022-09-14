from rest_framework import serializers

from movies.models import Genre, Movie, MovieNight
from movienight_auth.models import User



class GenreField(serializers.SlugRelatedField):
    def to_internal_value(self, data):
        try:
            return self.get_queryset().get_or_create(name=data.lower())[0]
        except (TypeError, ValueError):
            self.fail(f"Tag value {data} is invalid")


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["name"]


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreField(slug_field="name", many=True, read_only=True)
    class Meta:
        model = Movie
        fields = "__all__"


class MovieTitleUrlSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedRelatedField(
        view_name="movie_night_detail_ui",
        read_only=True
    )

    class Meta:
        model = Movie
        fields = ["title", "url"]

# class MovieNightInvitationSerilazier(serializers.ModelSerializer):
#     class Meta:
#         pass

class MovieNightSerializer(serializers.ModelSerializer):
    movie = MovieTitleUrlSerializer(read_only=True)
    creator = serializers.HyperlinkedRelatedField(
        queryset = User.objects.all(), view_name="api_user_detail",
        lookup_field = "email",
    )
    # invites = MovieNightInvitationSerilazier()

    class Meta:
        model = MovieNight
        fields = "__all__"