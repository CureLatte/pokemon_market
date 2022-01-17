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


# @bp.route('/')
# def load_make_new_page():
#     token_receive = request.cookies.get('mytoken')
#     if token_receive is not None:
#         return render_template('profile.html')
#     else:
#         return render_template('sign_in.html')

@bp.route('/home', methods=['GET'])
def open_profile():
    user = db.users.find_one({'user_id': 'qwer1'})
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

    title = title[::-1]
    photo = photo[::-1]
    date = date[::-1]
    monster = monster[::-1]
    # print(user['poket_box'][0])
    return render_template('profile.html', container=user, mon_title=title, mon_photo=photo, mon_date=date,
                           get_mon=monster, monster=pokemon)
