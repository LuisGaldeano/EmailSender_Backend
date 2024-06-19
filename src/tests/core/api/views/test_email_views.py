from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from core.api.serializers import EmailSerializer, TemplateSerializer
from core.factories import EmailFactory, TemplateFactory, UserFactory
from core.models import Email, EmailTemplate


class TemplateListCreateViewTestCase(APITestCase):
    url = reverse("core:template")

    def test_list_200_ok(self):
        initial_template: EmailTemplate = TemplateFactory()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [TemplateSerializer(initial_template).data])

    def test_create_201_created(self):
        data_to_sent = {"name": "test_template"}
        self.assertEqual(EmailTemplate.objects.count(), 0)
        response = self.client.post(self.url, data_to_sent)
        self.assertEqual(EmailTemplate.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, TemplateSerializer(EmailTemplate.objects.last()).data)


class EmailListCreateViewTestCase(APITestCase):
    url = reverse("core:email")

    def test_list_200_ok(self):
        initial_email: Email = EmailFactory()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [EmailSerializer(initial_email).data])

    def test_create_201_created(self):
        template: EmailTemplate = TemplateFactory()
        receiver: User = UserFactory()
        data_to_sent = {"email": receiver.email, "template_uuid": template.uuid.hex}
        self.assertEqual(Email.objects.count(), 0)
        response = self.client.post(self.url, data_to_sent)
        self.assertEqual(Email.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, EmailSerializer(Email.objects.last()).data)
