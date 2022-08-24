from django.urls import reverse

import pytest
from rest_framework import status

from apps.shortener.models import Link

pytestmark = pytest.mark.django_db


class TestLinkViewSet:
    def test_create_ok(self, client, mocker):
        mocked_short = mocker.patch(
            "apps.shortener.models.Link.generate_short", return_value="ujdnt"
        )
        url = reverse("api:links-list")
        data = {"full": "http://example.com/very-very/long/url/even-longer"}
        response = client.post(url, data, format="json")
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json() == {"short": "http://testserver/api/links/ujdnt"}
        assert Link.objects.count() == 1
        assert (
            Link.objects.get().full
            == "http://example.com/very-very/long/url/even-longer"
        )
        assert Link.objects.get().short == "ujdnt"
        mocked_short.assert_called_once()

    def test_create_invalid_data(self, client):
        url = reverse("api:links-list")
        data = {"full": "xxx"}
        response = client.post(url, data, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json() == {"full": ["Enter a valid URL."]}
        assert Link.objects.count() == 0

    def test_retrieve_ok(self, client):
        Link.objects.create(
            full="http://example.com/very-very/long/url/even-longer", short="tywiq"
        )
        url = reverse("api:links-detail", args=["tywiq"])
        response = client.get(url)
        assert response.status_code == status.HTTP_302_FOUND
        assert response.url == "http://example.com/very-very/long/url/even-longer"

    def test_retrieve_not_found(self, client):
        Link.objects.create(
            full="http://example.com/very-very/long/url/even-longer", short="tywiq"
        )
        url = reverse("api:links-detail", args=["iksmd"])
        response = client.get(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.json() == {"error": "Link with this short does not exist"}
