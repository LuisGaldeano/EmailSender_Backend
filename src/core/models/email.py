from django.forms import CharField
from django.db import models
from core.models.abstract import TimeStampedUUIDModel
from core.models.client import Client


class Email(TimeStampedUUIDModel):
    NEWMAIL = 'new'
    ALLOWED_TEMPLATES = (
        (NEWMAIL, 'new_email'),
    )
    template = models.CharField(
        choices=ALLOWED_TEMPLATES,
        blank=True,
        null=True,
    )

    extra_parameters = CharField(
        null=True,
        blank=True
    )

    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    custom_data = CharField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.template, self.client
