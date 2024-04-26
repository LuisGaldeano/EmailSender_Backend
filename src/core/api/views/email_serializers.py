from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from core.api.serializers.email_serializers import EmailSerializer
from core.models.email import Email


class CreateNewEmailView(CreateAPIView):
    serializer_class = EmailSerializer
    queryset = Email.objects.all()
    permission_classes = [IsAuthenticated]
