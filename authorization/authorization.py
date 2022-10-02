import datetime
import json
import jwt
from flask import request
from flask import Flask


def serializer(message):
    return json.dumps(message).encode('utf-8')

app = Flask(__name__)
file = open("list-devices.json")
devices = json.load(file)


@app.route("/token",methods =['POST'])
def get_token():
    device_found = None
    for device in devices:
        if device['id']  == request.json.get('id', None):
            device_found = device
    if device_found is None:
        return 'Device not found', 401
    timestamp = datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(seconds=30)
    base_token = {
        'iat': timestamp,
        'exp': timestamp + datetime.timedelta(seconds=30),
        'sub': device_found['id'],
        'iss': 'www.test.com',
        'permissions': device_found['permissions']
    }
    encoded_jwt = jwt.encode(base_token, "secret", algorithm="HS256")
    response = {'token': encoded_jwt}
    return response, 200

@app.route("/valid",methods =['POST'])
def valid_token():
    try:
        token = request.json.get('token', None)
        decode = jwt.decode(token, "secret", algorithms=["HS256"])
        response = {
            'valid': True,
            'permissions': decode['permissions']
        }
        return response, 200
    except:
        response = {
            'valid': False
        }
        return response, 401


if __name__ == "__main__":
    app.run(debug=True, port = 5000)