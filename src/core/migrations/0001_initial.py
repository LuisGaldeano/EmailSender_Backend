# Generated by Django 5.0.3 on 2024-05-21 11:34

import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="EmailTemplate",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="modified"
                    ),
                ),
                ("uuid", models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                (
                    "name",
                    models.TextField(
                        db_index=True,
                        help_text="The name of the template.",
                        max_length=128,
                        unique=True,
                        verbose_name="Name",
                    ),
                ),
            ],
            options={
                "verbose_name": "Template",
                "verbose_name_plural": "Templates",
            },
        ),
        migrations.CreateModel(
            name="Email",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="modified"
                    ),
                ),
                ("uuid", models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                (
                    "sent",
                    models.BooleanField(default=False, help_text="Whether the email was sent.", verbose_name="Sent"),
                ),
                (
                    "error_message",
                    models.TextField(
                        blank=True,
                        help_text="If the message was not sent, this is the error message related.",
                        null=True,
                        verbose_name="Error message",
                    ),
                ),
                (
                    "receiver",
                    models.ForeignKey(
                        help_text="User that will receive the email.",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="emails",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Receiver",
                    ),
                ),
                (
                    "template",
                    models.ForeignKey(
                        help_text="Template used to render the email. This is the one that the consumer must handle.",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="emails",
                        to="core.emailtemplate",
                        verbose_name="Template",
                    ),
                ),
            ],
            options={
                "verbose_name": "Email",
                "verbose_name_plural": "Emails",
            },
        ),
    ]
