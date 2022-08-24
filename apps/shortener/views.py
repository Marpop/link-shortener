from django.http import HttpResponseRedirect

from rest_framework import status
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.shortener import serializers
from apps.shortener.models import Link


class LinkViewSet(CreateModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Link.objects.all()
    serializer_class = serializers.LinkSerializer
    lookup_field = "short"

    def get_full_uri(self, request, url):
        return request.build_absolute_uri(url)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        link = Link.objects.create(
            full=serializer.validated_data["full"], short=Link.generate_short()
        )

        headers = self.get_success_headers(serializer.data)
        return Response(
            {"short": self.get_full_uri(request, link.short)},
            status=status.HTTP_201_CREATED,
            headers=headers,
        )

    def retrieve(self, request, short=None):
        try:
            link = Link.objects.get(short=short)
            url = self.get_full_uri(request, link.full)
            return HttpResponseRedirect(redirect_to=url)
        except Link.DoesNotExist:
            return Response(
                {"error": "Link with this short does not exist"},
                status=status.HTTP_404_NOT_FOUND,
            )
