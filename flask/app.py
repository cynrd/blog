#!/usr/bin/python3
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/users/<string:user_name>')
def get_user(user_name):
    return jsonify({'hello': user_name})

if __name__ == '__main__':
    app.run(debug=True)
