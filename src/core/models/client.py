from django.contrib.auth.models import AbstractUser
from django.forms import CharField
from django.db import models
from core.models.abstract import TimeStampedUUIDModel


class Client(AbstractUser, TimeStampedUUIDModel):
    name = CharField(
        null=True,
        blank=True)
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    firm = models.CharField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.email
