import tensorflow as tf
from flask import Blueprint
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from flask import request
from flask import jsonify
from static.model.poketmon_class import poket_all_class
from flask import redirect, url_for
import datetime
import os
from pathlib import PureWindowsPath
from pymongo import MongoClient
import certifi
import shutil

ca = certifi.where()

client = MongoClient("mongodb+srv://test:sparta@cluster0.cpg4z.mongodb.net/Cluster0?retryWrites=true&w=majority", tlsCAFile=ca)

db = client.dbpokemon

SECRET_KEY = 'sparta'
model = tf.keras.models.load_model('./static/model/model_SGD_add_1.h5')
bp = Blueprint("machine", __name__, url_prefix='/machine')


@bp.route('/load', methods=['POST'])
def save_picture_to_time():
    root_path = os.path.abspath(__file__)
    # Path 객체로 변환
    p = PureWindowsPath(root_path)
    # 절대 경로로 변환 해줌
    img_storage = str(p.parents[1])+'\\static\\image\\pokemons\\'
    if os.path.exists(img_storage):
        shutil.rmtree(img_storage)
    os.mkdir(img_storage)

    file = request.files['file_give']
    # 해당 파일에서 확장자명만 추출
    extension = file.filename.split('.')[-1]
    if extension != 'png' and extension != 'jpg' and extension != 'jpeg':
        return jsonify({'result': '확장자를 확인해주세요'})

    # 파일 이름이 중복되면 안되므로, 지금 시간을 해당 파일 이름으로 만들어서 중복이 되지 않게 함!
    today = datetime.datetime.now()
    mytime = today.strftime('%Y-%m-%d-%H-%M-%S')
    filename = f'{mytime}'
    # 파일 저장 경로 설정 (파일은 서버 컴퓨터 자체에 저장됨)
    save_to = f'\\static\\image\\pokemons\\{filename}.{extension}'
    # 현재 파일의 경로 파악

    last_path = str(p.parents[1]) + save_to
    # 파일 저장!
    file.save(last_path)
    return redirect((url_for('machine.predict_poketmon')))


@bp.route('/result')
def predict_poketmon():
    test_datagen = ImageDataGenerator(rescale=1. / 255)
    # 이미지가 모여있는 폴더
    test_dir = './static/image'
    test_generator = test_datagen.flow_from_directory(
        test_dir,
        # target_size 는 학습할때 설정했던 사이즈와 일치해야 함
        target_size=(224, 224),
        color_mode="rgb",
        shuffle=False,
        # test 셋의 경우, 굳이 클래스가 필요하지 않음
        # 학습할때는 꼭 binary 혹은 categorical 로 설정해줘야 함에 유의
        class_mode=None,
        batch_size=1)
    pred = model.predict(test_generator)
    max_value = max(pred[-1])
    print(max_value)
    if max_value <= 0.7:
        return jsonify({'result': 'none'})
    for index, k in enumerate(pred[-1]):
        if k == max_value:
            result = poket_all_class[index]
            break
    return jsonify({'result': result})


