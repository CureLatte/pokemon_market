from flask import Blueprint
from flask import request
from flask import jsonify
from flask import redirect, url_for, render_template
import jwt
from flask import Flask
from pymongo import MongoClient
import certifi
from datetime import datetime

ca = certifi.where()

client = MongoClient("mongodb+srv://test:sparta@cluster0.cpg4z.mongodb.net/Cluster0?retryWrites=true&w=majority", tlsCAFile=ca)

db = client.dbpokemon

bp = Blueprint("sort_pokemon", __name__, url_prefix='/sort_pokemon')
app = Flask(__name__)
app.secret_key = 'sparta'


def check_decode():
    token_receive = request.cookies.get('mytoken')
    if token_receive is not None:
        try:
            payload = jwt.decode(token_receive, app.secret_key, algorithms=['HS256'])
            return payload['user_id']
        except:
            return None
    else:
        return None


@bp.route('/<category>/<page_number>', methods=['GET'])
def token_check(category, page_number):
    user_id = check_decode()
    if user_id is not None:
        page_all = 5*10
        container = list(db.market.find({'category': category}))
        container.sort(key=lambda x: x['date'], reverse=True)
        time_all = datetime.now()

        return render_template('sort_pokemon.html', container=container, curr_day=time_all.day, curr_hour=time_all.hour)
    else:
        return redirect(url_for('main'))
