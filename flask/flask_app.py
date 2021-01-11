from flask import Flask
from time import sleep
from os import getpid

DELAY = 2

sleep(5)  # demonstrate slow app time with graceful reload

app = Flask(__name__)


@app.route('/')
def hello_world():
    sleep(DELAY)
    return str(getpid())
