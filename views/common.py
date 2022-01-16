from flask import Blueprint
from flask import request
from flask import jsonify
from flask import redirect, url_for, render_template
import jwt
from flask import Flask

bp = Blueprint("common", __name__, url_prefix='/common')
app = Flask(__name__)
app.secret_key = 'sparta'


def check_decode():
    token_receive = request.cookies.get('mytoken')
    if token_receive is not None:
        try:
            payload = jwt.decode(token_receive, app.secret_key, algorithms=['HS256'])
            return payload['user_id']
        except:
            return None
    else:
        return None


@bp.route('/token_check', methods=['GET'])
def token_check():
    token_receive = request.cookies.get('mytoken')
    try:
        if token_receive is not None:
            payload = jwt.decode(token_receive, app.secret_key, algorithms=['HS256'])
            return jsonify({'user_id': payload['user_id']})
        else:
            return jsonify({'user_id': 'None'})

    except jwt.ExpiredSignatureError:
        return redirect(url_for("sign_in", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return render_template('sign_in.html')
