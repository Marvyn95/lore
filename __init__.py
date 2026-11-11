from flask import Flask
import json
import pymongo

with open('../config.json') as config_file:
    config = json.load(config_file)

app = Flask(__name__)
app.config['SECRET_KEY'] = config['SECRET_KEY']
db = pymongo.MongoClient(config['MONGODB_URI']).lore_database

import routes