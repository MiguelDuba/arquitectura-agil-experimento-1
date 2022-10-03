import datetime
import json
import requests
from flask import request, Flask
    
app = Flask(__name__)

@app.route("/notification",methods =['POST'])
def send_notification():
    try:
        token = request.json.get('token', None)

        headers = {'content-type': 'application/json'}
        response  = requests.post(
            'http://127.0.0.1:5000/valid', headers=headers, data=json.dumps({
                'token': token
            })
        )

        if response.status_code == 200:
            res = response.json()
            if 'notification' in res['permissions']:
                return {'send': True }, 200

        return {'send': False }, 401
    except:
        return {'send': False }, 401

if __name__ == "__main__":
    app.run(debug=True, port = 5001)