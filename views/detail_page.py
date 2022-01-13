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
    "mongodb+srv://<id>:<password>>@cluster0.kgq1f.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client.dbpokemon

# 해당 페이지의 접두어를 넣고 이동하면 됩니다.
bp = Blueprint("detail_page", __name__, url_prefix='/detail_page')

# 실제 URL : localhost:5000/detail_page


@bp.route('/')
def detail_page():
    # 다른 주소로 보낼 떄 : redirect(url_for('블루프린트이름.함수이름'))
    return render_template("detail_page.html")
