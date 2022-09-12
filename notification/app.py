import json
import uuid
from datetime import datetime
from flask import Flask, request
from kafka import KafkaConsumer, KafkaProducer

def serializer(message):
    return json.dumps(message).encode('utf-8')

app = Flask(__name__)
producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=serializer)


@app.route("/event", methods = ['POST'])
def create_event():
    now = datetime.now()
    event = {
        'id': uuid.uuid4(),
        'value': request.json.get('value', 0),
        'place': request.json.get('place', 'ERROR_GETTING_PLACE'),
        'timespamp': datetime.timestamp(now)
    }
    producer.send('', event)
    return "Event Created",200

if __name__ == '__main__':
    app.run(debug=True, port = 5000)


