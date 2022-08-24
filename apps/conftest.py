import pytest
from rest_framework.test import APIClient


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def api_client():
    return APIClient()
