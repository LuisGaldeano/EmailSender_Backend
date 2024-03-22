from django.contrib.auth.models import AbstractUser
from django.forms import CharField
from django.db import models
from core.models.abstract import TimeStampedUUIDModel


class User(AbstractUser, TimeStampedUUIDModel):
    JUNIOR, MID, SENIOR = 'j', 'm', 's'
    ALLOWED_ROLES = (
        (JUNIOR, 'Junior'),
        (MID, 'Mid'),
        (SENIOR, 'Senior'),
    )
    name = CharField(
        null=True,
        blank=True)
    email = models.EmailField(
        null=True
    )
    role = models.CharField(
        choices=ALLOWED_ROLES,
        blank=True,
        null=True,
    )
