from os import environ
from flask import Flask 

app = Flask(__name__)

@app.route('/', methods=['GET'])
def getData():
    return 'ok'

if __name__ == '__main__':
    port = environ['PORT'] if 'PORT' in environ else '8080'
    app.run('localhost', port, debug=True)
