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
from views.common import check_decode
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

    owner_user = db.users.find_one({"user_id": maket["user_id"]}, {'_id': False})
    print(owner_user)
    if maket is None:
        return redirect(url_for('main_page.main_page'))
    else:
        return render_template('detail_page.html', maket=maket, owner_user=owner_user)


@bp.route('/random_test', methods=['POST'])
def random_api():
    user_id = check_decode()
    if user_id is not None:
        market_id = request.form['aaa']
        container = db.market.find_one({'maket_id':market_id},{'_id':False})
        category_list = list(db.market.find({'category':container['category']},{'_id':False}))
        return jsonify({'user_interest': category_list})
    else:
        return jsonify({'user_interest': 'none'})



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





@bp.route('/trade', methods=['POST'])
def trade():
    sc_receive = request.form["sc_give"]
    price_receive = int(request.form["price_give"])
    seller_receive = request.form["seller_give"]
    logedin_receive = request.form["logedin_give"]
    seller = db.users.find_one(
        {"user_id": seller_receive})
    logein_user = db.users.find_one(
        {"user_id": logedin_receive})

    seller_poketmon = db.market.find_one({"maket_id": sc_receive})

    seller_point = int(seller["point"])
    logein_user_point = int(logein_user["point"])

    sp = seller_point + price_receive  # 파는사람 포인트 최종
    lp = logein_user_point - price_receive  # "사는사람 포인트 최종

    if lp < 0:
        return jsonify({'msg': '보유중인 포인트가 부족합니다!'})

    # 나중에 93번에 포켓몬 이름 들어오도록 나중에 수정
    db.users.update_one({"user_id": seller_receive}, {"$set": {"point": sp}})
    db.users.update_one({"user_id": logedin_receive}, {"$set": {"point": lp}})
    db.users.update_one(
        {"user_id": logein_user["user_id"]},
        {
            "$push": {
                "poket_box":
                {
                    "포켓몬 이름 들어오도록 나중에 수정": seller_poketmon["photo"]
                }
            }
        }
    )
    db.market.delete_one({"maket_id": sc_receive})
    return jsonify({'msg': '등록완료'})


@bp.route('/api/like', methods=['POST'])
def like_api():
    id_receive = request.form['id_give']
    target = db.market.find_one({'user_id': id_receive})

    target_list = target['like_list']
    current_like = target['like']

    if id_receive in target_list:
        sub_like = current_like - 1
        db.market.update({'user_id': id_receive}, {'$pull': {'like_list': id_receive}})
        db.market.update_one({'user_id': id_receive}, {'$set': {'like': sub_like}})

    else:
        add_like = current_like + 1
        db.market.update({'user_id': id_receive}, {'$addToSet': {'like_list': id_receive}})
        db.market.update_one({'user_id': id_receive}, {'$set': {'like': add_like}})

    now_like = target['like']

    return jsonify({'like_num': now_like})


# @bp.route('/random', methods=['POST'])
# def random_api():
#     print('random IN!')
#     id_receive = request.form["id_give"]
#     interest = db.users.find_one({'user_id': id_receive})['interest_poket']
#     match = list(db.market.find({'category': interest}, {'_id': False}))
#     return jsonify({'user_interest': match})


