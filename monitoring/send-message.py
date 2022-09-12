import json
import uuid
from flask import request
from flask import Flask
from kafka import KafkaProducer


app = Flask(__name__)

def serializer(message):
    return json.dumps(message).encode('utf-8')

@app.route("/sendMessage",methods =['POST'])
def send_message():
    id_message= str(uuid.uuid4())
    producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=serializer)
    monitoring = {
        'id': id_message,
    }
    producer.send('monitoring_request', monitoring)
    return "Message sended with id "+ id_message, 200

if __name__ == "__main__":
    app.run(debug=True, port = 5000)