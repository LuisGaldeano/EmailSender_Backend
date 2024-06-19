from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView

from core.api.serializers import UserSerializer


class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
