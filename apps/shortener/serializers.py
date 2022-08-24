from rest_framework import serializers

from apps.shortener.models import Link


class LinkReduceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ["full"]


class LinkExpandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ["short"]
