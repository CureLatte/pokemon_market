# from views import detail_page
import hashlib

from flask import Flask, render_template, jsonify, request, Blueprint
from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient(
    "mongodb+srv://test:sparta@cluster0.cpg4z.mongodb.net/Cluster0?retryWrites=true&w=majority", tlsCAFile=ca)

SECRET_KEY = 'sparta'

bp = Blueprint("sign_up", __name__, url_prefix='/sign_up')

db = client.dbpokemon


@bp.route('/')
def main():
    return render_template('sign_up.html')


@bp.route('/submit', methods=['POST'])
def sign_up_submit():
    receive_user = request.form.to_dict()
    avatar_img= request.form['interest_poket'] +'.png'

    receive_user['password'] = hashlib.sha256(
        receive_user['password'].encode('utf-8')).hexdigest()
    receive_user['avatar'] = avatar_img
    receive_user['point'] = 5000

    db.users.insert_one(receive_user)

    return jsonify({'msg': '회원가입 완료!'})


@bp.route('/pokemon_search', methods=['GET'])
def sign_up_pokemon_search():
    category = db.category.find_one({}, {'_id': False, 'poket_category': 1})
    return jsonify({'category': category})


@bp.route('/user_id', methods=['POST'])
def sign_up_check_user_id():
    user_id = request.form['user_id']

    all_user_id = list(db.users.find({}, {'_id': False, 'user_id': 1}))

    is_user_id = True

    for temp_id in all_user_id:
        if user_id in temp_id['user_id']:
            is_user_id = False

    return jsonify({'is_user_id': is_user_id})