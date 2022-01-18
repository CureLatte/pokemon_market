import uuid

from flask import render_template, Flask
from flask import request
from flask import Blueprint
from flask import make_response
from flask import jsonify
from flask import url_for
from pymongo import MongoClient
from pathlib import Path

from flask import redirect
from functools import wraps

import requests
import jwt
import hashlib
import requests
import test
import random
from datetime import datetime
import os
from pathlib import PureWindowsPath
import certifi

ca = certifi.where()
client = MongoClient("mongodb+srv://test:sparta@cluster0.cpg4z.mongodb.net/Cluster0?retryWrites=true&w=majority",
                     tlsCAFile=ca)
db = client.dbpokemon

SECRET_KEY = 'sparta'
app = Flask(__name__)

bp = Blueprint("make_new", __name__, url_prefix='/make_new')


@bp.route('/')
def load_make_new_page():
    token_receive = request.cookies.get('mytoken')
    if token_receive is not None:
        return render_template('upload_pokemon.html')
    else:
        return render_template('sign_in.html')


@bp.route('/upload', methods=['POST'])
def upload_db_data():
    desc_receive = request.form['desc_give']
    photo = request.files['photo_give']
    title = request.form['title_give']
    price = request.form['price_give']
    result = request.form['result_give']
    user_id = request.form['id_give']

    level = request.form['level_give']
    like_feed = request.form['like_feed_give']
    catch_location = request.form['catch_location_give']
    trade_location = request.form['trade_location_give']

    if price == "":
        price = ""
    else:
        price = price
    extension = photo.filename.split('.')[-1]
    today = datetime.now()
    mytime = today.strftime('%Y-%m-%d-%H-%M-%S')
    filename = f'{mytime}.{extension}'
    save_to = f'\\static\\image\\content\\{filename}'

    root_path = os.path.abspath(__file__)
    a = PureWindowsPath(root_path)
    abs_path = str(a.parents[1]) + save_to

    photo.save(abs_path)
    i = uuid.uuid1()
    c = {
        'maket_id': str(i),
        'user_id': user_id,
        'content': '',
        'comment':
            [
                {
                    'photo_user_id': '',
                    'photo_comment': '',
                    'photo_avatar': ''
                }
            ],
        'category': result,
        'photo': filename,
        'desc': desc_receive,
        'header': title,
        'date': mytime,
        'price': price,
        'level': level,
        'like_feed': like_feed,
        'catch_location': catch_location,
        'trade_location': trade_location,
        'like': 0,
        'like_list': []
    }
    db.market.insert_one(c)

    return jsonify({'msg': '등록완료'})
