from flask import Flask

# Create a server object and register it with import name __name__ (so that extensions etc can identify Flask)
# Our docker image expects the flask instance to be called 'app'
app = Flask(__name__)


# Assign a path to say_hello
@app.route('/hello')
def say_hello():
    """Say hello"""
    return "Hello new World"


# Assign new path to say hello to a specific person
@app.route('/hello/<name>')
def say_hello_to(name):
    """Say hello to a specific person"""
    return 'Hello %s' % name


if __name__ == '__main__':
    # Start the server in standalone mode
    app.run()
