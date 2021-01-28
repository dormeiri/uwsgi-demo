# uwsgi-demo

Demonstrates the main features and concepts of the uWSGI server

## Requirements

1. Install Python 3
1. Install virtual environment (recommended)
1. Install uWSGI

## Pure

"Hello, World!" app for the uWSGI server, contains pure WSGI implementation with basic uWSGI configurations

## Flask

"Hello, World!" app for Flask server (which implements WSGI) with more advanced uWSGI configurations

## Stress test

Use the `stresstest.py` to demonstrate high traffic to the uWSGI server, you can run it using `python -m stresstest.py`

## How-to and tips

1. In order to start the uWSGI server, `cd` to the folder that contains the `uwsgi.ini` and run `uwsgi uwsgi.ini` in your terminal
1. Use `uwsgitop` to monitor your workers in real time
1. Play with the configurations! Using the `touch-reload` option, your app will be reloaded when updating the `uwsgi.ini` file
