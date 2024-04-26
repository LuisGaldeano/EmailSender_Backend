from django.db import models

from core.models import ClientUser
from core.models.abstract import TimeStampedUUIDModel


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

    extra_parameters = models.CharField(
        blank=True,
        null=True,
    )

    client = models.ForeignKey(ClientUser, on_delete=models.CASCADE)

    custom_data = models.CharField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.template, self.client
