from rest_framework import serializers

from movies.models import Genre, Movie, MovieNight, MovieNightInvitaion
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
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreField(slug_field="name", many=True, read_only=True)
    class Meta:
        model = Movie
        fields = "__all__"
        read_only_fields = [
            "title", "year", "runtime_minutes",
            "imdb_id", "genres", "plot",
            "is_full_record",
        ]


class MovieTitleUrlSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedRelatedField(
        view_name="movie_night_detail_ui",
        read_only=True
    )

    class Meta:
        model = Movie
        fields = ["title", "url"]


class MovieNightInvitationSerilazier(serializers.ModelSerializer):
    invitee = serializers.HyperlinkedRelatedField(
        view_name="api_user_detail",
        read_only=True,
        lookup_field = "email",
    )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["info"] = instance.__str__
        return representation

    class Meta:
        model = MovieNightInvitaion
        fields = "__all__"
        read_only_fields = ["attendance_confirmed", "movie_night", "invitee"]



class MovieNightSerializer(serializers.ModelSerializer):
    movie = MovieTitleUrlSerializer(read_only=True)
    creator = serializers.HyperlinkedRelatedField(
        view_name="api_user_detail",
        read_only=True,
        lookup_field = "email",
    )
    invites = MovieNightInvitationSerilazier(read_only=True, many=True)

    class Meta:
        model = MovieNight
        fields = "__all__"
        read_only_fields = ["movie", "creator", "start_notification_sent", "invites"]


class MovieSearchSerilazier(serializers.Serializer):
    term = serializers.CharField()