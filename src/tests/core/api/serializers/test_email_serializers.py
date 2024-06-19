import uuid
from unittest.mock import MagicMock, patch

from core.api.serializers import EmailSerializer, TemplateSerializer, UserSerializer
from core.exceptions.api import NotFoundException
from core.factories import EmailFactory, TemplateFactory, UserFactory
from core.models import Email, EmailTemplate
from tests.helpers import SerializerTestBase


class TemplateSerializerTestCase(SerializerTestBase):
    def test_data(self):
        template: EmailTemplate = TemplateFactory()
        expected_data = {"uuid": template.uuid.hex, "name": template.name}
        self.assertEqual(TemplateSerializer(instance=template).data, expected_data)


class EmailSerializerTestCase(SerializerTestBase):
    def test_data(self):
        email: Email = EmailFactory(sent=True, error_message="test_error")
        expected_data = {
            "uuid": email.uuid.hex,
            "template": TemplateSerializer(email.template).data,
            "receiver": UserSerializer(email.receiver).data,
            "sent": True,
            "error_message": "test_error",
        }
        self.assertEqual(EmailSerializer(instance=email).data, expected_data)

    @patch("core.models.Email.send", MagicMock())
    def test_create_valid_instance(self):
        template = TemplateFactory()
        user = UserFactory(email="test@example.com")
        data = {
            "email": "test@example.com",
            "template_uuid": template.uuid.hex,
        }

        serializer = EmailSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        self.assertEqual(instance.receiver, user)
        self.assertEqual(instance.template, template)
        self.assertTrue(Email.send.called)

    @patch("core.models.Email.send", MagicMock())
    def test_create_email_not_found_raises_not_found_exception(self):
        template = TemplateFactory()
        data = {
            "email": "nonexistent@example.com",
            "template_uuid": template.uuid.hex,
        }

        serializer = EmailSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        with self.assertRaises(NotFoundException) as expected_exception:
            serializer.save()

        self.assertEqual(
            expected_exception.exception.detail,
            "Email 'nonexistent@example.com' not found in database.",
        )
        self.assertFalse(Email.send.called)

    @patch("core.models.Email.send", MagicMock())
    def test_create_template_not_found_raises_not_found_exception(self):
        UserFactory(email="test@example.com")
        fake_uuid = uuid.uuid4()
        data = {
            "email": "test@example.com",
            "template_uuid": fake_uuid,
        }

        serializer = EmailSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        with self.assertRaises(NotFoundException) as expected_exception:
            serializer.save()

        self.assertEqual(
            expected_exception.exception.detail,
            f"Template '{fake_uuid}' not found in database.",
        )
        self.assertFalse(Email.send.called)
