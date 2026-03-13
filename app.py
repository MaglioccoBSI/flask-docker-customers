from flask import flask
import os

app = Flask(__name__)

customer = os.getenv('CUSTOMER', 'default')

@app.route('/')
def index():
    return f'Hello, {customer}!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
    