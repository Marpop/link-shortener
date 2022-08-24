import pytest

from apps.shortener.models import Link, get_random_string

pytestmark = pytest.mark.django_db


class TestLink:
    def setup(self):
        self.link = Link.objects.create(full="http://example.com", short="abcde")

    def test__get_random_string(self):
        assert len(get_random_string()) == 5
        assert len(get_random_string(length=5)) == 5
        assert len(get_random_string(length=6)) == 6

    def test__generate_short(self, mocker):
        mocked_random = mocker.patch(
            "apps.shortener.models.get_random_string", return_value="jnsiq"
        )
        assert self.link._generate_short() == "jnsiq"
        mocked_random.assert_called_once()
