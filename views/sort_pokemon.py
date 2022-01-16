from flask import Blueprint
from flask import request
from flask import jsonify
from flask import redirect, url_for, render_template
import jwt
from flask import Flask
from pymongo import MongoClient
import certifi
from datetime import datetime
from views.common import check_decode

ca = certifi.where()

client = MongoClient("mongodb+srv://test:sparta@cluster0.cpg4z.mongodb.net/Cluster0?retryWrites=true&w=majority", tlsCAFile=ca)

db = client.dbpokemon

bp = Blueprint("sort_pokemon", __name__, url_prefix='/sort_pokemon')
app = Flask(__name__)
app.secret_key = 'sparta'


@bp.route('/<category>/<page_number>')
def token_check(category, page_number):
    user_id = check_decode()
    print(user_id)
    if user_id is not None:
        page_all = 5*10
        container = list(db.market.find({'category': category}))
        container.sort(key=lambda x: x['date'], reverse=True)
        time_all = datetime.now()
        return render_template('sort_pokemon.html', container=container, curr_day=time_all.day, curr_hour=time_all.hour)
    else:
        return redirect(url_for('main'))
