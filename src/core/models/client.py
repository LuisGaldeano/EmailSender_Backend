from django.db import models
from core.models.abstract import TimeStampedUUIDModel


class ClientUser(TimeStampedUUIDModel):
    name = models.CharField(
        null=True,
        blank=True)
    client_email = models.EmailField(
        max_length=255,
        unique=True,
    )
    firm = models.CharField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.client_email
