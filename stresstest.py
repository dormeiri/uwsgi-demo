import threading
import requests
from sys import argv
import time

URL = 'http://localhost:9090'
lock = threading.Lock()


class RequestThread(threading.Thread):
    def __init__(self, id):
        super().__init__()
        self.duration = 0
        self.id = id

    def run(self):
        self.log('requesting...')
        start_time = time.perf_counter()
        response = requests.get(URL)
        self.duration = time.perf_counter() - start_time
        self.log(f'response: {response.content}')

    def log(self, message):
        lock.acquire()
        print(self.id, round(self.duration, 2), message, sep='\t')
        lock.release()


def main():
    times = int(argv[1]) if len(argv) > 1 else 1
    for i in range(times):
        RequestThread(str(i)).start()


if __name__ == '__main__':
    main()
