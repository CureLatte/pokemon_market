import datetime
from flask import render_template
from flask import request
from flask import Blueprint
from flask import make_response
from flask import jsonify
from flask import url_for
from pymongo import MongoClient
from flask import redirect
from functools import wraps
import requests
import jwt
import hashlib
# import requests

client = MongoClient(
    "mongodb+srv://test:sparta@cluster0.cpg4z.mongodb.net/Cluster0?retryWrites=true&w=majority")

db = client.dbpokemon
# 해당 페이지의 접두어를 넣고 이동하면 됩니다.
bp = Blueprint("detail_page", __name__, url_prefix='/detail_page')


# 실제 URL : localhost:5000/detail_page

@bp.route('/<maket_id>')
def load_my_feed(maket_id):
    maket = db.market.find_one({'maket_id': maket_id}, {'_id': False})
    owner_user = db.users.find_one(
        {"user_id": maket["user_id"]}, {'_id': False})
    if maket is None:
        return render_template('not_found_detail.html')

    else:
        return render_template('detail_page.html', maket=maket, owner_user=owner_user)


@bp.route('/', methods=['POST'])
def upload_comment():
    logedin_receive = request.form["logedin_give"]
    sc_receive = request.form["sc_give"]
    comment_receive = request.form['comment_give']
    find_logein_user = db.users.find_one(
        {"user_id": logedin_receive})["avatar"]

    test = {"photo_user_id": logedin_receive,
            "photo_comment": comment_receive,
            "photo_avatar": find_logein_user,
            }

    update_feed = ({"maket_id": sc_receive},
                   {
        "$push": {"comment": test}
    })

    db.market.update_one(*update_feed)

    return jsonify({'msg': '등록완료'})
