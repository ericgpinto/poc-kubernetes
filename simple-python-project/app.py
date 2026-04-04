import os
from flask import Flask
from datetime import datetime

app = Flask(__name__)
start_time = datetime.now()

@app.route('/')
def hello():
    name = os.getenv('NAME')
    age = os.getenv('AGE')
    return f'Hello, my name is {name} and I am {age} years old.'

@app.route('/secret')
def secret():
    user = os.getenv('USER')
    password = os.getenv('PASSWORD')
    return f'User {user}. Password {password}'

@app.route('/healthz')
def healthz():
    duration = (datetime.now() - start_time).total_seconds()
    if(duration > 25):
        return 'Not healthy', 500
    else:     
        return 'Healthy', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)