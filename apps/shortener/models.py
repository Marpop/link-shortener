import random
from string import ascii_lowercase

from django.core.validators import URLValidator
from django.db import IntegrityError, models

RANDOM_STRING_LENGTH: int = 5
SHORT_MAX_LENGTH: int = 50


def get_random_string(length: int = RANDOM_STRING_LENGTH) -> str:
    return "".join(random.choice(ascii_lowercase) for _ in range(length))


class Link(models.Model):
    full = models.TextField(validators=[URLValidator()])
    short = models.CharField(
        max_length=SHORT_MAX_LENGTH,
        unique=True,
        db_index=True,
        validators=[URLValidator()],
    )

    def __save__(self, *args, **kwargs):
        if not self.short:
            self.short = self._generate_short()
        super().save(*args, **kwargs)

    def _generate_short(self) -> str:
        length = RANDOM_STRING_LENGTH
        short = get_random_string(length)
        while Link.objects.filter(short=short).exists():
            length += 1
            if length >= SHORT_MAX_LENGTH:
                raise IntegrityError("Could not generate unique short")
            short = get_random_string(RANDOM_STRING_LENGTH)
        return short
