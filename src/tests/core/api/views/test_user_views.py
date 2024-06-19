from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from core.api.serializers import UserSerializer
from core.factories import UserFactory


class UserListCreateViewTestCase(APITestCase):
    url = reverse("core:user")

    def test_list_200_ok(self):
        initial_user: User = UserFactory()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [UserSerializer(initial_user).data])

    def test_create_201_created(self):
        data_to_sent = {
            "username": "test_username",
            "password": "test_password",
            "email": "test_email@test.com",
            "first_name": "test_first_name",
            "last_name": "test_last_name",
        }
        self.assertEqual(User.objects.count(), 0)
        response = self.client.post(self.url, data_to_sent)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, UserSerializer(User.objects.last()).data)
