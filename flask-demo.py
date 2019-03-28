# This is a Flask approach.
# From https://towardsdatascience.com/deploying-a-machine-learning-model-as-a-rest-api-4a03b865c165
# However (see README-branch.md) I'll probably

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
# I don't understand which line commandeers the mouse pointer for the entire desktop. The preceding line
# alone doesn't, but apparently any following import does.
# import pickle
# import numpy as np

import os #PHILIP nonsense

# This is the first line where things go awry. What is this model? The flask stuff "just worked"
# after I used pip to install the library as per the README.
# Turns out it's trying to import from the flask-rest-setup/sentiment-clf/model.py file.

# https://stackoverflow.com/questions/8350853/how-to-import-module-when-module-name-has-a-dash-or-hyphen-in-it

setup = __import__("flask-rest-setup")
exit()
from model import NLPModel
app = Flask(__name__)
api = Api(app)
# create new model object
model = NLPModel()
# load trained classifier
clf_path = 'lib/models/SentimentClassifier.pkl'
with open(clf_path, 'rb') as f:
    model.clf = pickle.load(f)
# load trained vectorizer
vec_path = 'lib/models/TFIDFVectorizer.pkl'
with open(vec_path, 'rb') as f:
    model.vectorizer = pickle.load(f)

