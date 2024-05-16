import os

from rest_framework import serializers

from core.common.producer import MessageProducer
from core.models.email import Email


class EmailSerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField(format='hex', read_only=True)

    class Meta:
        model = Email
        fields = [
            'uuid', 'template', 'username', 'client_email', 'address'
        ]

    def create(self, validated_data):
        instance = super().create(validated_data)

        validated_data['template'] = instance.template
        validated_data['username'] = instance.username
        validated_data['client_email'] = instance.client_email
        validated_data['address'] = instance.address

        producer = MessageProducer(topic=os.getenv("TOPIC"), group_id='test_group')
        producer.send_message(validated_data)

        return instance
