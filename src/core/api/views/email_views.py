from rest_framework.generics import ListCreateAPIView
from core.api.serializers.email_serializers import EmailSerializer
from core.models.email import Email


class CreateNewEmailView(ListCreateAPIView):
    serializer_class = EmailSerializer
    queryset = Email.objects.all()

