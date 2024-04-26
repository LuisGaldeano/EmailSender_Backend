from django.contrib.auth.models import User
from django.forms import CharField
from django.db import models
from core.models.abstract import TimeStampedUUIDModel


class EmailUser(User, TimeStampedUUIDModel):
    JUNIOR, MID, SENIOR = 'j', 'm', 's'
    ALLOWED_ROLES = (
        (JUNIOR, 'Junior'),
        (MID, 'Mid'),
        (SENIOR, 'Senior'),
    )
    role = models.CharField(
        choices=ALLOWED_ROLES,
        blank=True,
        null=True,
    )
