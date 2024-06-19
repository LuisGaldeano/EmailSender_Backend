from django.contrib.auth.models import User
from rest_framework import serializers

from core.api.serializers import UserSerializer
from core.exceptions.api import NotFoundException
from core.models.email import Email, EmailTemplate


class TemplateSerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField(format="hex", read_only=True)

    class Meta:
        model = EmailTemplate
        fields = ["uuid", "name"]


class EmailSerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField(format="hex", read_only=True)
    template = TemplateSerializer(read_only=True)
    receiver = UserSerializer(read_only=True)

    email = serializers.EmailField(write_only=True)
    template_uuid = serializers.UUIDField(write_only=True, format="hex")

    class Meta:
        model = Email
        fields = [
            "uuid",
            "template",
            "receiver",
            "sent",
            "error_message",
            "email",
            "template_uuid",
        ]

    def create(self, validated_data):
        email_to_check = validated_data.pop("email")
        if receiver := User.objects.filter(email=email_to_check):
            validated_data["receiver"] = receiver.first()
        else:
            raise NotFoundException(message=f"Email '{email_to_check}' not found in database.")

        template_uuid_to_check = validated_data.pop("template_uuid")
        if template := EmailTemplate.objects.filter(uuid=template_uuid_to_check):
            validated_data["template"] = template.first()
        else:
            raise NotFoundException(message=f"Template '{template_uuid_to_check}' not found in database.")

        instance: Email = super().create(validated_data)
        instance.send()
        return instance
