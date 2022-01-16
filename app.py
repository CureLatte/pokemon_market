from flask import Flask
from flask import render_template, request, redirect, jsonify, url_for
from pymongo import MongoClient

from views import upload_pokemon
import certifi
from views import model_test, common, sign_in, upload_pokemon,sign_up, detail_page, main_page

import jwt

ca = certifi.where()

client = MongoClient(
    "mongodb+srv://test:sparta@cluster0.cpg4z.mongodb.net/Cluster0?retryWrites=true&w=majority", tlsCAFile=ca)

app = Flask(__name__)
app.secret_key = 'sparta'

db = client.dbpokemon

# 블루프린트 등록하는 부분 app.register_blueprint(파일이름.bp)

app.register_blueprint(model_test.bp)
app.register_blueprint(common.bp)
app.register_blueprint(sign_in.bp)
app.register_blueprint(upload_pokemon.bp)
app.register_blueprint(sign_up.bp)
app.register_blueprint(detail_page.bp)
app.register_blueprint(main_page.bp)



@app.route('/')
def main():
    token_receive = request.cookies.get('mytoken')
    if token_receive is not None:
        return render_template('palette.html')
    else:
        return render_template('sign_in.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)
