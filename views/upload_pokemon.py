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
# Blueprint( 블루프린트 이름, __name__, url_prefix='url 접두어')
# 해당 페이지의 접두어를 넣고 이동하면 됩니다.
bp = Blueprint("upload_pokemon", __name__, url_prefix='/upload_pokemon')


# 실제 URL : Localhost:5000/templates/
@bp.route('/')
def upload():
    return render_template('upload_pokemon.html')


# 실제 URL : Localhost:5000/upload_pokemon/upload
@bp.route('/', methods=['POST'])
def upload_pokemon():
    desc_receive = request.form['desc_give']
    photo = request.files['photo_give']
    title = request.form['title_give']
    price = request.form['price_give']
    result = request.form['result_give']
    user_id = request.form['id_give']
    if price == "":
        price = ""
    else:
        price = price

    extension = photo.filename.split('.')[-1]
    today = datetime.now()
    mytime = today.strftime('%Y-%m-%d-%H-%M-%S')
    filename = f'{mytime}.{extension}'
    save_to = f'\\static\\image\\{filename}'

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
        'price': price
    }
    db.market.insert_one(c)

    return jsonify({'msg': '등록완료'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)
