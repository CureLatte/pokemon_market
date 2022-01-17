from pymongo import MongoClient
import jwt
import datetime
from flask import Flask, render_template, jsonify, request, session, redirect, url_for, Blueprint
import hashlib
import certifi
ca = certifi.where()

app = Flask(__name__)
app.secret_key = 'sparta'

client = MongoClient("mongodb+srv://test:sparta@cluster0.cpg4z.mongodb.net/Cluster0?retryWrites=true&w=majority", tlsCAFile=ca)
db = client.dbpokemon

bp = Blueprint("sign_in", __name__, url_prefix='/sign_in')


@bp.route('/login', methods=['POST'])
def api_login():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']

    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()
    result = db.users.find_one({'user_id': id_receive, 'password': pw_hash})

    if result is not None:
        payload = {
            'user_id': id_receive,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=12400)
        }
        token = jwt.encode(payload, app.secret_key, algorithm='HS256')
        return jsonify({'result': 'success', 'token': token})
    else:
        return jsonify({'result': 'fail'})
