from flask import Flask

# create a server object and register it with import name __name__ (so that extensions etc can identify Flask)
server = Flask(__name__)


# Assign a path to say_hello
@server.route('/hello')
def say_hello():
    """Say hello"""
    return "Hello World"


if __name__ == '__main__':
    # Start the server in standalone mode
    server.run()
