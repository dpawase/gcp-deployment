from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello from Cloud Function!', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

