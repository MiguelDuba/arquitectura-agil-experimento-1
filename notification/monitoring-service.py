from datetime import datetime
import json
import uuid
from kafka import KafkaConsumer, KafkaProducer

def serializer(message):
    return json.dumps(message).encode('utf-8')
service_name =  str(uuid.uuid4())
consumer = KafkaConsumer('monitoring_request',bootstrap_servers='localhost:9092')
producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=serializer)
print('Service name '+ service_name)
print('Kafka Consumer, Producer has been initiated...')

if __name__ == '__main__':
    for msg in consumer:
        print('Monitoring message received')
        monitoring_request = json.loads(msg.value)
        monitoring_response = {
            'id': monitoring_request.get('id'),
            'service_name': service_name,
            'status': 'Ok',
            'type': 'Notification',
            'timespamp': datetime.timestamp(datetime.now())
        }
        producer.send('monitoring_response', monitoring_response)
        print('Monitoring message response')