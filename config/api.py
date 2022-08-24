from django.urls import include, path

urlpatterns = [
    path("links/", include(("apps.shortener.urls", "links"))),
]
