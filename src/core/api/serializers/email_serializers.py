from rest_framework import serializers

from core.models.email import Email


class EmailSerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField(format='hex', read_only=True)
    template = serializers.SerializerMethodField(read_only=True)
    extra_parameters = serializers.SerializerMethodField(read_only=True)
    client_email = serializers.SerializerMethodField(read_only=True)
    custom_data = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Email
        fields = [
            'uuid', 'template', 'extra_parameters', 'client', 'custom_data'
        ]

    def create(self, validated_data):
        username = validated_data.pop('extra_parameters', None).get('username')
        address = validated_data.pop('custom_data', None).get('address')
        email = Email.objects.create(**validated_data)

        if username is not None and address is not None:
            email.extra_parameters = username
            email.custom_data = address
            email.save()

        return email
