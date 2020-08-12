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

s3 = os.environ['SECRET']
#s3 = SECRET

# name of database
app.config['MONGO_DBNAME'] = 'joiners'

# URI of database
app.config['MONGO_URI'] = f'mongodb+srv://join:{s3}@cluster0.fnifx.mongodb.net/joiners?retryWrites=true&w=majority'

mongo = PyMongo(app)

# DICTIONARY
item_keywords = {
    "DT1":"Dome Tour Trading Cards (B1)",
    "FFCarat": "Fallin Flower Carat ver. Photocards",
    "DTPola1": "Dome Tour Polaroid Cards (White ver) + Unit Cards",
    "HMV1": "Heng:garae HMVs (B1)",
    "Haru1": "Haru Trading Cards (B1)",
    "HMV2": "Heng:garae HMVs (B2)",
    "Carrot1": "Ideal Cut Japan Carrot Cards (B1)",
    "DTHolo1": "Dome Tour Holographic Cards (B1)",
    "3FS2": "AppleMusic/MusicArt Fansign Photocards (B2)",
    "4FS2": "Soundwave/M2U Fansign Photocards (B2)",
    "DTHolo2": "Dome Tour Holographic Cards (B2)",
    "2FS":"Synnara/Hottracks Fansign Photocards",
    "FFReg":"Fallin Flower Regular ver. Photocards",
    "DTPola2":"Dome Tour Polaroid Cards (white ver)",
    "Carrot2":"Ideal Cut Japan Carrot Cards (B2)",
    "OTYPola":"Ode to You Japan Polaroid Cards",
    "DTPolaColor":"Dome Tour Polaroid Cards (color/sign ver)",
    "OTYLen":"Ode to You Japan Lenticular Cards",
    "DTHolo3":"Dome Tour Holographic Cards (B3)",
    "3FS3":"AppleMusic/MusicArt Fansign Photocards (B3)",
    "4FS3":"Soundwave/M2U Fansign Photocards (B3)",
    "Haru2":"Haru Trading Cards (B2)",
    "1FS": "Yes24/Interpark Fansign Photocards",
    "DT2":"Dome Tour Trading Cards (B2)",
    "4FS1":"Soundwave/M2U Fansign Photocards (B1)",
    "OTY":"Ode to You Japan Trading Cards",
    "FFJosh":"Fallin Flower Joshua Photocards",
    "HGFansign":"Album + Fansign PC GO",
    "personalorder":"Personal Order",
    "Kihno":"Heng:garae Kihno Cards",
    "3FS":"AppleMusic/MusicArt Fansign Photocards"
}

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
        joiner = joiners.find({'username':request.form['search'].lower()})
        existing_joiner = list(joiner)
        if existing_joiner:
            wow = list(existing_joiner)
            info = wow[0]
            info2 = info['items']
            return render_template('index.html', info = info, info2 = info2, time = datetime.now(), item_key = item_keywords)
        else:
            error = "That username doesn't exist. Please try again or contact me if you think there is a mistake."
            return render_template('index.html', error = error)
    return render_template('index.html', time = datetime.now())

# @app.route('/test')
# def test():
#     csv_columns = ['Username','Status','Location']
#     joiners = mongo.db.joiners
#     existing_joiner = joiners.find({})
#     info = list(existing_joiner)
#     dict_data = []
#     for user in info:
#         new_user = {
#             'Username': user['username'],
#             'Status': "",
#             'Location': user['location'].upper()
#         }
#         dict_data.append(new_user)

#     currentPath = os.getcwd()
#     csv_file = currentPath + "/csv/Names.csv"

#     WriteDictToCSV(csv_file, csv_columns, dict_data)
#     return "worked"