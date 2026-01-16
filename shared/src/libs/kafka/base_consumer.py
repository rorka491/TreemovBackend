import json
from kafka import KafkaConsumer as KC
from shared.contracts.email import EmailEvent
from typing import Callable

class BaseConsumer:
    def __init__(
        self,
        topic: str,
        handler: Callable[[EmailEvent], None],
        bootstrap_servers=None,
        group_id: str = "default-group"
    ):
        self.consumer = KC(
            topic,
            bootstrap_servers=bootstrap_servers or ['localhost:9092'],
            value_deserializer=lambda v: json.loads(v.decode('utf-8')),
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id=group_id
        )
        self.handler = handler

    def start(self):
        print(f"[Kafka Consumer] Подписка на топик {self.consumer.subscription()}")
        for message in self.consumer:
            data = message.value
            try:
                event = EmailEvent(**data)
                self.handler(event)
            except Exception as e:
                print(f"[Kafka Consumer] Ошибка при обработке сообщения: {e}")
