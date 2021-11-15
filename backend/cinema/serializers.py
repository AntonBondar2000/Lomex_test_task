from django.db.models import (
    Avg,
    Count
)
from rest_framework import serializers
from cinema.models import (
    Actor,
    Movie
)


class ActorListSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()
    best_genre = serializers.SerializerMethodField()

    class Meta:
        model = Actor
        fields = [
            'name',
            'movies_count',
            'best_genre'
        ]

    def get_movies_count(self, inst):
        return Movie.objects.filter(actors=inst).count()

    def get_best_genre(self, inst):
        best_genre = Movie.objects.filter(
            actors=inst
        ).annotate(
            star=Avg('imdb_rating')
        ).order_by('-star')
        return best_genre[0].genre


class GenreListSerializer(serializers.Serializer):
    genre = serializers.CharField()
    movies_count = serializers.SerializerMethodField()
    avg_rating = serializers.SerializerMethodField()

    def get_movies_count(self, inst):
        return Movie.objects.filter(genre=inst['genre']).count()

    def get_avg_rating(self, inst):
        data = Movie.objects.filter(
            genre=inst['genre']
        ).aggregate(Avg('imdb_rating'))
        return data['imdb_rating__avg']


class DirectorListSerializer(serializers.Serializer):
    director = serializers.CharField()
    best_movies = serializers.SerializerMethodField()
    favourite_actors = serializers.SerializerMethodField()

    def get_best_movies(self, inst):
        return Movie.objects.filter(
            director=inst['director']
        ).order_by(
            '-imdb_rating'
        ).values_list(
            'title', flat=True
        )[:3]

    def get_favourite_actors(self, inst):
        movies = Movie.objects.filter(
            director=inst['director']
        ).values_list('actors')
        actors = Actor.objects.exclude(
            name=""
        ).filter(
            movie__actors__in=movies
        ).annotate(
            count=Count('name')
        ).order_by(
            '-count'
        ).values_list(
            'name', 'count'
        )[:3]
        return actors