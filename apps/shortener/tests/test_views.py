from django.urls import reverse

import pytest
from rest_framework import status

from apps.shortener.models import Link

pytestmark = pytest.mark.django_db


class TestLinkReduceView:
    def test_k(self, client):
        url = reverse("links:link-reduce")
        data = {"full": "https://www.google.com"}
        response = client.post(url, data, format="json")
        assert response.status_code == status.HTTP_201_CREATED
        assert Link.objects.count() == 1
        assert Link.objects.get().full == "https://www.google.com"
        assert len(Link.objects.get().short) == 5

    def test_invalid_data(self, client):
        url = reverse("links:link-reduce")
        data = {"full": "xxx"}
        response = client.post(url, data, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json() == {"full": ["Enter a valid URL."]}
        assert Link.objects.count() == 0
