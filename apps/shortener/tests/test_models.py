import pytest

from apps.shortener.models import Link, get_random_string

pytestmark = pytest.mark.django_db


class TestLink:
    def test_get_random_string(self):
        assert len(get_random_string()) == 5
        assert len(get_random_string(length=5)) == 5
        assert len(get_random_string(length=6)) == 6

    def test__generate_short(self):
        link = Link.objects.create()
        short = link._generate_short()
        assert len(short) == 5
