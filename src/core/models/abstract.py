import uuid

from django.db import models
from model_utils.models import TimeStampedModel


class UUIDModel(models.Model):
    uuid = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        abstract = True


class TimeStampedUUIDModel(UUIDModel, TimeStampedModel):
    class Meta:
        abstract = True
