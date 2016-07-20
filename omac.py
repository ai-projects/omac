"""
OMAC - OMnipotent Artificial Companion

Omac is an artificial intelligence assistant developed for make easier ongoing daily task
around dates, contacts and scheduling.

"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
