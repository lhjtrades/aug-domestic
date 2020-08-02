# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask_pymongo import PyMongo
from datetime import datetime
import os


# -- Initialization section --
app = Flask(__name__)

app.config['SECRET'] = os.getenv("SECRET_KEY")
SECRET = app.config['SECRET']

# name of database
app.config['MONGO_DBNAME'] = 'joiners'

# URI of database
app.config['MONGO_URI'] = f'mongodb+srv://admin_2:{SECRET}@cluster0.fnifx.mongodb.net/joiners?retryWrites=true&w=majority'

mongo = PyMongo(app)

# -- Routes section --
# INDEX

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", time = datetime.now())

@app.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        joiners = mongo.db.joiners
        existing_joiner = joiners.find_one({'username' : request.form['search']})
        info = dict(existing_joiner)
        info2 = existing_joiner['items']
        if existing_joiner is None:
            return render_template('index.html', time = datetime.now())
        return render_template('index.html', info = info, info2 = info2, time = datetime.now())
    return render_template('index.html', time = datetime.now())
