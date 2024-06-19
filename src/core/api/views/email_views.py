from rest_framework.generics import ListCreateAPIView

from core.api.serializers.email_serializers import EmailSerializer, TemplateSerializer
from core.models import Email, EmailTemplate


class TemplateListCreateView(ListCreateAPIView):
    serializer_class = TemplateSerializer
    queryset = EmailTemplate.objects.all()


class EmailListCreateView(ListCreateAPIView):
    serializer_class = EmailSerializer
    queryset = Email.objects.all()
