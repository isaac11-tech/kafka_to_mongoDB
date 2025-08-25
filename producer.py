from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

message = {"msg": "Hello Kafka from Python!"}
producer.send("test-topic", message)

print("Message sent:", message)
producer.flush()
producer.close()
