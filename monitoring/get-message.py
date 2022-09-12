import json
from kafka import KafkaConsumer
consumer = KafkaConsumer('monitoring_response',bootstrap_servers='localhost:9092')
print('Kafka Consumer has been initiated...')

responses={}

if __name__ == '__main__':
    for msg in consumer:
        message_response = json.loads(msg.value)
        response = responses.get(message_response.get('id'), None)
        if response is None:
            id = message_response.get('id')
            new_response = [{'service':message_response.get('service_name'), 'status': message_response.get('status'), 'timespamp':message_response.get('timespamp'), 'type':message_response.get('type')}]
            responses[id] = new_response
        else:
            response.append({'service':message_response.get('service_name'), 'status': message_response.get('status'), 'timespamp':message_response.get('timespamp'),'type':message_response.get('type')})
        #print(responses)
        if message_response.get('status') != 'Ok':
            print('ERROR instance ' + message_response.get('service_name') + ' for '+message_response.get('type')+' has error PLEASE CHECK IT status '+ message_response.get('status'))
