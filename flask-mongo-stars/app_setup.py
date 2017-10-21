#!/usr/bin/python3
from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'restdb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/restdb'

mongo = PyMongo(app)

@app.route('/_pact/provider_states', methods=['POST'])
def provider_states():
    mapping = {'no_stars': no_stars,
               'sirius': sirius}
    mapping[request.json['state']]()
    return jsonify({'result': request.json['state']})

def no_stars():
  star = mongo.db.stars
  star.drop()

def sirius():
  star = mongo.db.stars
  star.drop()
  name = 'Sirius'
  distance = 8.6
  star_id = star.insert({'name': name, 'distance': distance})
  new_star = star.find_one({'_id': star_id })
  output = {'name' : new_star['name'], 'distance' : new_star['distance']}

if __name__ == '__main__':
    app.run(debug=True, port=5001)
