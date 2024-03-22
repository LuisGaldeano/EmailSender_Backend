import os
import json
from confluent_kafka import Producer


class MessageProducer(Producer):
    def __init__(self, topic: str, group_id: str):
        self.broker_host = os.getenv("KAFKA_BROKER_URL")
        self.broker_port = os.getenv("KAFKA_BROKER_PORT")
        self.topic = topic
        super().__init__(
            {
                'bootstrap.servers': f"{self.broker_host}:{self.broker_port}",
                'group.id': group_id,
                'auto.offset.reset': 'earliest'
            }
        )

    def send_message(self, message_data):
        message = json.dumps(message_data)
        self.produce(
            topic=self.topic,
            value=message.encode('utf-8')
        )
        self.flush()
