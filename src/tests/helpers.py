from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIRequestFactory

from core.factories import UserFactory


class SerializerTestBase(TestCase):
    def setUp(self) -> None:
        self.user: User = UserFactory()
        self.request = APIRequestFactory().post("/foo", data=None)
        self.request.user = self.user
        self.context = {"request": self.request}
