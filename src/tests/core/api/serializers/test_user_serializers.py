from django.contrib.auth.models import User

from core.api.serializers import UserSerializer
from core.factories import UserFactory
from tests.helpers import SerializerTestBase


class UserSerializerTestCase(SerializerTestBase):
    def test_data(self):
        user: User = UserFactory()
        expected_data = {
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
        }
        self.assertEqual(UserSerializer(instance=user).data, expected_data)

    def test_create_create_user(self):
        data = {
            "username": "test",
            "email": "test@test.com",
            "first_name": "test",
            "last_name": "test",
            "password": "test_password",
        }
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        instance: User = serializer.save()
        self.assertTrue(instance.check_password("test_password"))
        self.assertEqual(instance.email, "test@test.com")
        self.assertEqual(instance.username, "test")
        self.assertEqual(instance.first_name, "test")
        self.assertEqual(instance.last_name, "test")
