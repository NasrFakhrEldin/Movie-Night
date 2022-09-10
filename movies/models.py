from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

UserModel = get_user_model()

class SearchTerm(models.Model):
    class Meta:
        ordering = ["id"]
    
    term = models.TextField(unique=True)
    last_search = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.term


class Genre(models.Model):
    class Meta:
        ordering = ["name"]

    name = models.TextField(unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    class Meta:
        ordering = ["title", "year"]

    title = models.TextField()
    year = models.PositiveIntegerField()
    runtime_minutes = models.PositiveIntegerField(null = True)
    imdb_id = models.SlugField(unique=True)
    genres = models.ManyToManyField(Genre, related_name="movies")
    plot = models.TextField(null=True, blank=True)
    is_full_record = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({self.year})"


class MovieNight(models.Model):
    class Meta:
        ordering = ["creator", "start_time"]

    movie = models.ForeignKey(Movie, on_delete=models.PROTECT)
    start_time = models.DateTimeField()
    creator = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.movie} by {self.creator.email}"