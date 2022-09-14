from django.urls import path, include

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

from movienight_auth.api.views import UserDetail
# from rest_framework.authtoken import views

from movies.api.views import (
    GenreViewSet, MovieViewSet,
    MovieNightViewSet
)

router = DefaultRouter()
router.register("movie-nights", MovieNightViewSet, basename="movienight")
router.register("movies", MovieViewSet)
router.register("genres", GenreViewSet)

urlpatterns = [
    path("users/<str:email>", UserDetail.as_view(), name="api_user_detail"),
]
urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    # path("auth/", include("rest_framework.urls")),
    # path("token-auth/", views.obtain_auth_token),
    path("", include(router.urls)),
]