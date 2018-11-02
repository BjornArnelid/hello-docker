import os

from flask import Flask, jsonify
from pymongo import MongoClient


if os.environ.get('MONGOHOST'):
    mongo_host = os.environ.get('MONGOHOST')
else:
    mongo_host = 'localhost'

# Create a server object and register it with import name __name__ (so that extensions etc can identify Flask)
# Our docker image expects the flask instance to be called 'app'
app = Flask(__name__)


# Assign a path to say_hello
@app.route('/hello')
def say_hello():
    """Say hello"""
    return "Hello World"


# Assign new path to say hello to a specific person
@app.route('/hello/<name>')
def say_hello_to(name):
    """Say hello to a specific person"""

    # Connect and increment database, if it does not exist it will be created
    db = MongoClient(mongo_host, 27017).hello_db
    db.counts.find_one_and_update({'name': name}, {'$inc': {'count': 1}}, upsert=True)
    # Say hello
    return 'Hello %s' % name


@app.route('/count/<name>')
def count_hellos(name):
    """Count number of hellos to person"""

    # Connect to database and fetch counter
    db = MongoClient(mongo_host, 27017).hello_db
    calls = db.counts.find_one({'name': name}).get('count')

    # if document exist return number, otherwise return no calls
    if calls:
        return '%d calls' % calls
    else:
        return 'No calls'


if __name__ == '__main__':
    # Start the server in standalone mode
    app.run()
