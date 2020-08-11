# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask_pymongo import PyMongo
from datetime import datetime
from model import WriteDictToCSV
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
    return render_template('index.html')
    #     existing_joiner = joiners.find_one({'username' : request.form['search']})
    #     info = dict(existing_joiner)
    #     info2 = existing_joiner['items']
    #     if existing_joiner is None:
    #         return render_template('index.html', time = datetime.now())
    #     else:
    #         return render_template('index.html', info = info, info2 = info2, time = datetime.now())
    # else:
    #     return render_template('index.html', time = datetime.now())

@app.route('/test')
def test():
    csv_columns = ['Username','Email']
    joiners = mongo.db.joiners
    existing_joiner = joiners.find({})
    info = list(existing_joiner)
    dict_data = []
    for user in info:
        new_user = {
            'Username': user['username'],
            'Email': user['email']
        }
        dict_data.append(new_user)

    currentPath = os.getcwd()
    csv_file = currentPath + "/csv/Names.csv"

    WriteDictToCSV(csv_file, csv_columns, dict_data)
    return "worked"