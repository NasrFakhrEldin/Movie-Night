from django.contrib import admin
from movies.models import Genre, Movie, SearchTerm, MovieNight, MovieNightInvitaion
# Register your models here.
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(SearchTerm)
admin.site.register(MovieNight)
admin.site.register(MovieNightInvitaion)