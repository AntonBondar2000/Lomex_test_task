from django.contrib import admin
from cinema.models import (
    Actor,
    Writer,
    Movie
)


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    pass


@admin.register(Writer)
class ActorAdmin(admin.ModelAdmin):
    pass


@admin.register(Movie)
class ActorAdmin(admin.ModelAdmin):
    search_fields = ['title']
