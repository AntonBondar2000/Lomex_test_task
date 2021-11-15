from rest_framework.response import Response
from rest_framework.viewsets import (
    ViewSet,
    ReadOnlyModelViewSet
)
from cinema.mixins import DataPaginationMixin
from cinema.models import (
    Actor,
    Movie
)
from cinema.serializers import (
    ActorListSerializer,
    GenreListSerializer,
    DirectorListSerializer
)


class GenreViewSet(ViewSet):
    def list(self, request):
        queryset = list(set(
            Movie.objects.values_list('genre', flat=True)
        ))[:20]
        queryset = [{'genre': item} for item in queryset]
        serializer = GenreListSerializer(queryset, many=True)
        return Response(serializer.data)


class ActorViewSet(ReadOnlyModelViewSet):
    queryset = Actor.objects.exclude(name='')
    serializer_class = ActorListSerializer
    pagination_class = DataPaginationMixin


class DirectorViewSet(ViewSet):
    def list(self, request):
        queryset = list(set(
            Movie.objects.exclude(director='').values_list('director', flat=True)
        ))[:20]
        queryset = [{'director': item} for item in queryset]
        serializer = DirectorListSerializer(queryset, many=True)
        return Response(serializer.data)
