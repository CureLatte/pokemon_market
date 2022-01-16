import hashlib, time
from datetime import datetime

from flask import Flask, render_template, jsonify, request, Blueprint,redirect,url_for
from pymongo import MongoClient
import certifi
from views.common import check_decode
from static.model.poketmon_class import poket_all_class

ca = certifi.where()

client = MongoClient(
    "mongodb+srv://test:sparta@cluster0.cpg4z.mongodb.net/Cluster0?retryWrites=true&w=majority", tlsCAFile=ca)

bp = Blueprint("main_page", __name__, url_prefix='/main_page')

db = client.dbpokemon


@bp.route('/')
def main_page():
    login_user_id = check_decode()
    if login_user_id is None:
        return redirect(url_for('main'))
    temp_poket = db.users.find_one({'user_id': login_user_id}, {'_id': False, 'interest_poket': 1})
    market_list = list(db.market.find({}, {'_id': False}))
    market_list.sort(key=lambda x: (x['date']), reverse=True)
    now = datetime.now()
    for market in market_list:
        temp_date = datetime.strptime(market['date'], '%Y-%m-%d-%H-%M-%S')
        temp_time = (now - temp_date)
        market['date'] = get_time(temp_time)


    # category 관련 작업 ##################
    BASE_CODE = 44032
    CHOSUNG = 588
    category_sort = sorted(poket_all_class.items(), key=lambda x: x[1])
    category_korean = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
    dict_by_letter = {}
    for index, poketmon_name in category_sort:
        string_list = list(poketmon_name)
        first_letter_index = int((ord(string_list[0]) - BASE_CODE) / CHOSUNG)
        if category_korean[first_letter_index] not in dict_by_letter:
            dict_by_letter[category_korean[first_letter_index]] = [poketmon_name]
        else:
            list_by_letter = dict_by_letter[category_korean[first_letter_index]]
            list_by_letter.append(poketmon_name)
    #####################################

    return render_template('main_page.html', market_list=market_list, login_interest_poket=temp_poket['interest_poket'], container=dict_by_letter, koreans=category_korean)


def get_time(tm):
    replace_hour = time.gmtime(tm.seconds).tm_hour
    replace_min = time.gmtime(tm.seconds).tm_min
    if tm.days > 0:
        replace_time = str(tm.days) + '일 전'
    elif replace_hour > 0:
        replace_time = str(replace_hour) + '시간 전'
    elif replace_min > 0:
        replace_time = str(replace_min) + '분 전'
    else:
        replace_time = '방금 전'

    return replace_time


@bp.route('/pokemon_search', methods=['GET'])
def main_page_pokemon_search():
    category = db.category.find_one({}, {'_id': False, 'poket_category': 1})
    return jsonify({'category': category})