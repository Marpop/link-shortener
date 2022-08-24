from django.urls import path

from apps.shortener import views

urlpatterns = [
    path("reduce/", views.LinkReduceView.as_view(), name="link-reduce"),
    path("expand/", views.LinkExpandView.as_view(), name="link-expand"),
]
