from flask import Blueprint
from flask import request
from flask import jsonify
from flask import redirect, url_for, render_template
from flask import Flask
import certifi
from pymongo import MongoClient

ca = certifi.where()

client = MongoClient(
    "mongodb+srv://test:sparta@cluster0.cpg4z.mongodb.net/Cluster0?retryWrites=true&w=majority", tlsCAFile=ca)
db = client.dbpokemon
bp = Blueprint("profile", __name__, url_prefix='/profile')
app = Flask(__name__)
app.secret_key = 'sparta'


@bp.route('/home', methods=['GET'])
def open_profile():
    user = db.users.find_one({'user_id': 'qwer2'})
    pokemon = list(db.market.find({'user_id': 'qwer1'}, {'_id': False}))
    title = []
    photo = []
    date = []
    monster = []

    for i in range(len(pokemon)):
        title.append(pokemon[i]['header'])
        photo.append(pokemon[i]['photo'])
        date.append(pokemon[i]['date'])

    for j in user['poket_box']:
        for i in j:
            monster.append(j[i])


    # print(user['poket_box'][0])
    return render_template('profile.html', container=user, mon_title=title, mon_photo=photo, mon_date=date, get_mon=monster)
