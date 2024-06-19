import os

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.common.producer import MessageProducer
from core.models import TimeStampedUUIDModel


class EmailTemplate(TimeStampedUUIDModel):
    name = models.TextField(
        max_length=128,
        unique=True,
        db_index=True,
        verbose_name=_("Name"),
        help_text=_("The name of the template."),
    )

    class Meta:
        verbose_name = _("Template")
        verbose_name_plural = _("Templates")
        app_label = "core"

    def __str__(self):
        return str(self.name)


class Email(TimeStampedUUIDModel):
    template = models.ForeignKey(
        EmailTemplate,
        db_index=True,
        on_delete=models.PROTECT,
        related_name="emails",
        verbose_name=_("Template"),
        help_text=_("Template used to render the email. This is the one that the consumer must handle."),
    )
    receiver = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="emails",
        verbose_name=_("Receiver"),
        help_text=_("User that will receive the email."),
    )
    sent = models.BooleanField(default=False, verbose_name=_("Sent"), help_text=_("Whether the email was sent."))
    error_message = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("Error message"),
        help_text=_("If the message was not sent, this is the error message related."),
    )

    class Meta:
        verbose_name = _("Email")
        verbose_name_plural = _("Emails")

    def send(self):
        try:
            producer = MessageProducer(topic=os.getenv("TOPIC"), group_id="test_group")
            producer.send_message(
                {
                    "template": self.template.name,
                    "username": self.receiver.username,
                    "client_email": self.receiver.email,
                }
            )
            self.sent = True
        except Exception as exception:
            self.error_message = str(exception)

        self.save()

    def __str__(self):
        return f"{self.template}-{self.receiver}"
