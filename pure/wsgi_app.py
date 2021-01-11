from time import sleep
from os import getpid


DELAY = 2


def application(env, start_response):
    sleep(DELAY)
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [str(getpid()).encode()]
