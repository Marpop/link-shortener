from rest_framework.routers import DefaultRouter

from apps.shortener.views import LinkViewSet

router = DefaultRouter()

router.register("links", LinkViewSet, basename="links")

app_name = "api"
urlpatterns = router.urls
