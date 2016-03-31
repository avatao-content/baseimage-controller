import os
from flask import Flask, jsonify, request
app = Flask(__name__)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ['CONTROLLER_PORT']),
            debug=(os.environ['DEBUG'].lower() == 'true'))
