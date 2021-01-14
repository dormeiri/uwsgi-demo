from flask import Flask
from time import sleep
from os import getpid


UP_TIME = 5
RESPONSE_TIME = 2


sleep(UP_TIME)  # demonstrates slow up time
app = Flask(__name__)


@app.route('/')
def hello_world():
    sleep(RESPONSE_TIME)  # demonstrates slow response time
    return str(getpid())

