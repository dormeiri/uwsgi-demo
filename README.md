# uwsgi-demo

![uWSGI demo](/uwsgi-demo.png?raw=true)

Demonstrates the main features and concepts of the uWSGI server

## Requirements

1. Install Python 3
1. Install virtual environment (recommended)
1. Install uWSGI

## How-to and tips

1. The [pure](pure) folder contains "Hello, World!" WSGI app with basic uWSGI configurations
1. The [flask](flask) folder contains "Hello, World!" Flask (which implements WSGI) app with more advanced uWSGI configurations
1. Use the [stresstest.py](stresstest.py) to demonstrate high traffic to the uWSGI server, you can run it using `python -m stresstest.py`
1. In order to start the uWSGI server, `cd` to the folder that contains the `uwsgi.ini` and run `uwsgi uwsgi.ini` in your terminal
1. Use `uwsgitop` to monitor your workers in real time
1. Play with the configurations! Using the `touch-reload` option, your app will be reloaded when updating the `uwsgi.ini` file
