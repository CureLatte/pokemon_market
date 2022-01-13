from flask import Flask
from flask import render_template,request,redirect,jsonify,url_for
from pymongo import MongoClient
# 작성해야하는 부분
from views import model_test
import jwt



client = MongoClient(
    "mongodb+srv://test:sparta@cluster0.cpg4z.mongodb.net/Cluster0?retryWrites=true&w=majority")

# 블루프린트 import 꼭 하기

app = Flask(__name__)
app.secret_key = 'sparta'

db = client.dbpokemon

# 블루프린트 등록하는 부분 app.register_blueprint(파일이름.bp)
app.register_blueprint(model_test.bp)


@app.route('/')
def main():
    return render_template('palette.html')


@app.route('/token_check', methods=['GET'])
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


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)
