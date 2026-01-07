import json
from kafka import KafkaProducer as KP
from shared.contracts.email import EmailEvent
from datetime import datetime, timezone

class BaseProducer:
    def __init__(self, bootstrap_servers=None):
        self.producer = KP(
            bootstrap_servers=bootstrap_servers or ['localhost:9092'],
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )

    def send(self, topic: str, event: EmailEvent):
        if not isinstance(event, EmailEvent):
            raise TypeError("event должен быть EmailEvent")
        
        self.producer.send(topic, event.dict())
        self.producer.flush()
        print(f"[Kafka Producer] Отправлено событие {event.event} в топик {topic}")
