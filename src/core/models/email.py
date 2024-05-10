from django.db import models

from core.models.abstract import TimeStampedUUIDModel


class Email(TimeStampedUUIDModel):
    NEWMAIL = 'new_email'
    ALLOWED_TEMPLATES = (
        (NEWMAIL, 'new_email'),
    )
    template = models.CharField(
        choices=ALLOWED_TEMPLATES,
        blank=True,
        null=True,
    )

    # user = models.ForeignKey(EmailUser, on_delete=models.CASCADE)

    username = models.CharField(
        blank=True,
        null=True,
    )

    client_email = models.EmailField(
        blank=True,
        null=True,
    )

    address = models.CharField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.template, self.client_email
