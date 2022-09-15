
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from movies.models import Genre, Movie, MovieNight, MovieNightInvitaion

from movies.api.serializers import (
    GenreSerializer, MovieSerializer,
    MovieNightSerializer, MovieNightInvitationSerilazier
)
from movies.api.permissions import IsInviteePermission, IsCreatorPermission



class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class MovieNightViewSet(viewsets.ModelViewSet):
    queryset = MovieNight.objects.all()
    serializer_class = MovieNightSerializer
    permission_classes = [IsAuthenticated & IsCreatorPermission]

class MovieNightInvitationViewset(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = MovieNightInvitationSerilazier
    permission_classes = [IsAuthenticated & IsInviteePermission]

    def get_queryset(self):
        return MovieNightInvitaion.objects.filter(invitee=self.request.user)