from rest_framework.routers import DefaultRouter
from cinema.views import (
    GenreViewSet,
    ActorViewSet,
    DirectorViewSet
)

router = DefaultRouter()
router.register(r'genres', GenreViewSet, basename='sections')
router.register(r'actors', ActorViewSet, basename='actors')
router.register(r'directors', DirectorViewSet, basename='directors')

urlpatterns = router.urls
