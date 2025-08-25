from kafka import KafkaConsumer
import json

class Consumer:

    def __init__(self,topic,host ='localhost:9092'):

        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=host,
            auto_offset_reset="earliest",
            enable_auto_commit=True,
            group_id="my-group",
            value_deserializer=lambda v: json.loads(v.decode('utf-8'))
        )

