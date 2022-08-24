from rest_framework import serializers

from apps.shortener.models import Link


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ["full"]
