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

client = MongoClient("mongodb+srv://test:sparta@cluster0.cpg4z.mongodb.net/Cluster0?retryWrites=true&w=majority", tlsCAFile=ca)

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

    db.market.update_one({'user_id': "qwer1"}, {'$set': {'photo': filename}})
    db.market.update_one({'user_id': "qwer1"}, {'$set': {'desc': desc_receive}})
    db.market.update_one({'user_id': "qwer1"}, {'$set': {'header': title}})
    db.market.update_one({'user_id': "qwer1"}, {'$set': {'date': mytime}})
    db.market.update_one({'user_id': "qwer1"}, {'$set': {'price': price}})
    # container_content = {

    # db.market.update_one({'user_id': user_info['user_id']}, {'$set': {'photo': filename}})
    # db.market.update_one({'user_id': user_info['user_id']}, {'$set': {'desc': desc_receive}})
    # db.market.update_one({'user_id': user_info['user_id']}, {'$set': {'header': title}})
    # db.market.update_one({'user_id': user_info['user_id']}, {'$set': {'date': today}})
    # db.market.update_one({'user_id': user_info['user_id']}, {'$set': {'price': price}})
    # # container_content = {
    #     'desc': desc_receive,
    #     'photo': filename,
    #     'comment': [],
    #     'like': 0,
    #     'like_user': []
    # }
    #
    # db.post_content.update_one({'user_id': user_info['user_id']}, {
    #     '$addToSet': {'container': container_content}})

    return jsonify({'msg': '등록완료'})
#
#
# # @bp.route('/upload_pokemon/confirming', methods=['POST'])
# # def pokemon_confirming():
# #     photo = request.files['photo_give']
# #     test_datagen = ImageDataGenerator(rescale=1. / 255)
# #     test_dir = photo
# #     test_generator = test_datagen.flow_from_directory(
# #         test_dir,
# #         # target_size 는 학습할때 설정했던 사이즈와 일치해야 함
# #         target_size=(256, 256),
# #         color_mode="rgb",
# #         shuffle=False,
# #         # test 셋의 경우, 굳이 클래스가 필요하지 않음
# #         # 학습할때는 꼭 binary 혹은 categorical 로 설정해줘야 함에 유의
# #         class_mode=None,
# #         batch_size=1)
# #     pred = model.predict(test_generator)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
