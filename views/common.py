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
import test

client = MongoClient(
    "mongodb+srv://<id>:<password>>@cluster0.kgq1f.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client.test

SECRET_KEY = 'sparta'

# Blueprint( 블루프린트 이름, __name__, url_prefix='url 접두어')
# 해당 페이지의 접두어를 넣고 이동하면 됩니다.
bp = Blueprint("auth", __name__, url_prefix='/templates')


# 실제 URL : Localhost:5000/templates/header

@bp.route('/header')
def test_api_function():
    return render_template('header.html')

# 실제 URL : Localhost:5000/templates/footer


@bp.route('/footer')
def test_api_function():
    return render_template('footer.html')
