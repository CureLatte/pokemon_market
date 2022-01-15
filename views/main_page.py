import hashlib, time
from datetime import datetime

from flask import Flask, render_template, jsonify, request, Blueprint
from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient(
    "mongodb+srv://test:sparta@cluster0.cpg4z.mongodb.net/Cluster0?retryWrites=true&w=majority", tlsCAFile=ca)

bp = Blueprint("main_page", __name__, url_prefix='/main_page')

db = client.dbpokemon


@bp.route('/')
def main_page():
    market_list = list(db.market.find({}, {'_id': False}))

    market_list.sort(key=lambda x: (x['date']), reverse=True)

    now = datetime.now()

    for market in market_list:
        temp_date = datetime.strptime(market['date'], '%Y-%m-%d-%H-%M-%S')
        temp_time = (now - temp_date)
        photo_time = lambda x: str(x.days) + '일 전' if (x.days > 0) else str(time.gmtime(x.seconds).tm_hour) + '시간 전'
        market['date'] = photo_time(temp_time)
        print(market['date'])

    return render_template('main_page.html', market_list=market_list)


@bp.route('/pokemon_search', methods=['GET'])
def main_page_pokemon_search():
    category = db.category.find_one({}, {'_id': False, 'poket_category': 1})
    return jsonify({'category': category})