from django.db import models


class Actor(models.Model):
    name = models.CharField(
        max_length=150,
        blank=True
    )

    class Meta:
        verbose_name = "Actor"
        verbose_name_plural = "Actors"
        ordering = ['name']

    def __str__(self):
        return self.name


class Writer(models.Model):
    id = models.CharField(
        max_length=27,
        primary_key=True
    )
    name = models.CharField(
        max_length=150,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Writer"
        verbose_name_plural = "Writers"
        ordering = ['name']

    def __str__(self):
        return self.name


class Movie(models.Model):
    id = models.TextField(
        primary_key=True
    )
    title = models.CharField(
        max_length=150
    )
    imdb_rating = models.FloatField()
    genre = models.CharField(
        max_length=150
    )
    description = models.TextField()
    writers = models.ManyToManyField(
        Writer
    )
    writers_names = models.TextField()
    director = models.CharField(
        max_length=150,
        blank=True,
        null=True
    )
    actors = models.ManyToManyField(
        Actor
    )
    actors_names = models.TextField()

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"
        ordering = ["title"]

    def __str__(self):
        return self.title
