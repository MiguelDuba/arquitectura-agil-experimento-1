# arquitectura-agil-experimento-1
## step #1
start kafka and zookeeper with the command
```
docker-compose up -d
```
## step #2
create env for pytohn
```
python -m venv venv
```
## step #3
activate venv 
```
venv\Scripts\activate
```
## step #4
init the environment for python
```
pip install -r requirements.txt
```
## step #5
start monitoring service for notifications
```
cd notification
python monitoring-service.py
```
## step #6
open a new terminal 
start monitoring to send notifications
```
cd monitoring
python send-message.py
```
With this we can send monitorin message using this CURL
```
POST /sendMessage HTTP/1.1
Host: localhost:5000
```
## step #7
open a new terminal 
start cmd to see the service with errors
```
cd monitoring
python python get-message.py
```
By default notification send ok in the request

To ineject the error modify the 
```
'status': 'Ok',
```
to 
```
'status': 'Error',
```
- run a new intance 
- make the request to send the messages
- and you will see the error in the get-message.py console
```
ERROR instance 1d0134f2-22d5-4c5b-9b5b-aaceaf17d8c2 for Notification has error PLEASE CHECK IT status Error
```