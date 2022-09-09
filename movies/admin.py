from django.contrib import admin
from movies.models import Genre, Movie, SearchTerm
# Register your models here.
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(SearchTerm)