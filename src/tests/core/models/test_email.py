from unittest import mock

from django.test import TestCase

from core.factories import EmailFactory
from core.models import Email


class EmailTestCase(TestCase):
    @mock.patch("core.models.email.MessageProducer")
    def test_send_ok(self, mock_producer):
        email: Email = EmailFactory()
        self.assertFalse(email.sent)
        email.send()
        self.assertTrue(email.sent)
        self.assertIsNone(email.error_message)
        self.assertEqual(mock_producer.call_count, 1)
        self.assertEqual(mock_producer().send_message.call_count, 1)
        self.assertEqual(
            mock_producer().send_message.call_args,
            mock.call(
                {
                    "template": email.template.name,
                    "username": email.receiver.username,
                    "client_email": email.receiver.email,
                }
            ),
        )

    @mock.patch("core.models.email.MessageProducer")
    def test_send_error(self, mock_producer):
        mock_producer.side_effect = Exception()
        email: Email = EmailFactory()
        self.assertFalse(email.sent)
        email.send()
        self.assertFalse(email.sent)
        self.assertIsNotNone(email.error_message)
