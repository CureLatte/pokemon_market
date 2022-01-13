from pymongo import MongoClient
import jwt
import datetime
from flask import Flask, render_template, jsonify, request, redirect, url_for, Blueprint
from datetime import datetime


app = Flask(__name__)

SECRET_KEY = 'sparta'

client = MongoClient("mongodb+srv://test:sparta@cluster0.cpg4z.mongodb.net/Cluster0?retryWrites=true&w=majority")
db = client.dbpokemon

bp = Blueprint("sign_in", __name__, url_prefix='/sign_in')


@bp.route('/')
def login_page():
    token_receive = request.cookies.get('mytoken')
    try:
        if jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256']):
            return render_template('page_0.html')

    except jwt.ExpiredSignatureError:
        return redirect(url_for("login_page", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return render_template('sign_in.html')


@bp.route('/sign_in', methods=['POST'])
def api_login():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']

    # pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    result = db.user.find_one({'user_id': id_receive, 'pwd': pw_receive})

    if result is not None:
        payload = {
            'user_id': id_receive,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=12400)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return jsonify({'result': 'success', 'token': token.decode('utf-8')})
    else:
        return jsonify({'result': 'fail'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)