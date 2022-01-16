from flask import Flask
from flask import render_template, request, redirect, jsonify, url_for
from pymongo import MongoClient
# 작성해야하는 부분
from views import model_test, common, sign_in, sort_pokemon
import jwt

client = MongoClient("mongodb+srv://test:sparta@cluster0.cpg4z.mongodb.net/Cluster0?retryWrites=true&w=majority")

app = Flask(__name__)
app.secret_key = 'sparta'

db = client.dbpokemon

app.register_blueprint(model_test.bp)
app.register_blueprint(common.bp)
app.register_blueprint(sign_in.bp)
app.register_blueprint(sort_pokemon.bp)


@app.route('/')
def main():
    token_receive = request.cookies.get('mytoken')
    if token_receive is not None:
        return render_template('palette.html')
    else:
        return render_template('sign_in.html')


@app.route('/main_page')
def goto_main():
    return render_template('palette.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)

