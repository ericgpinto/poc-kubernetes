import os
from flask import Flask

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)