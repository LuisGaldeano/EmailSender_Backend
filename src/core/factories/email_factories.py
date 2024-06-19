import factory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyText

from core.factories import UserFactory
from core.models import Email, EmailTemplate


class TemplateFactory(DjangoModelFactory):
    class Meta:
        model = EmailTemplate

    name = FuzzyText()


class EmailFactory(DjangoModelFactory):
    class Meta:
        model = Email

    template = factory.SubFactory(TemplateFactory)
    receiver = factory.SubFactory(UserFactory)
    sent = False
    error_message = None
