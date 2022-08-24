from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from apps.shortener import serializers
from apps.shortener.models import Link


class LinkReduceView(CreateAPIView):
    queryset = Link.objects.all()
    serializer_class = serializers.LinkReduceSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        link = self.perform_create(serializer)
        return Response(
            {"short": link.short},
            status=status.HTTP_201_CREATED,
            headers=self.get_success_headers(serializer.data),
        )


class LinkExpandView(CreateAPIView):
    queryset = Link.objects.all()
    serializer_class = serializers.LinkExpandSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        short = serializer.validated_data["short"]
        try:
            link = Link.objects.get(short=short)
        except Link.DoesNotExist:
            return Response(
                {"error": "Link with this short does not exist"},
                status=status.HTTP_404_NOT_FOUND,
            )
        return Response(
            {"full": link.full},
            status=status.HTTP_200_OK,
            headers=self.get_success_headers(serializer.data),
        )
