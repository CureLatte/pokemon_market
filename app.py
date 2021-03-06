from flask import Flask
from flask import render_template, request, redirect, jsonify, url_for
from pymongo import MongoClient
import certifi
from views import model_test, common, sign_in, upload_pokemon, sign_up, detail_page, main_page, category, sort_pokemon, profile

import jwt
import certifi
from pymongo import MongoClient

ca = certifi.where()
client = MongoClient("mongodb+srv://test:rlawotjd8250!@cluster0.cpg4z.mongodb.net/Cluster0?retryWrites=true&w=majority", tlsCAFile=ca)

db = client.test


app = Flask(__name__)
app.secret_key = 'sparta'

db = client.dbpokemon


app.register_blueprint(model_test.bp)
app.register_blueprint(common.bp)
app.register_blueprint(sign_in.bp)
app.register_blueprint(upload_pokemon.bp)
app.register_blueprint(sign_up.bp)
app.register_blueprint(detail_page.bp)
app.register_blueprint(main_page.bp)
app.register_blueprint(category.bp)
app.register_blueprint(sort_pokemon.bp)
app.register_blueprint(profile.bp)



@app.route('/')
def main():

    token_receive = request.cookies.get('mytoken')
    if token_receive is not None:
        return redirect(url_for('main_page.main_page'))
    else:
        return render_template('sign_in.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
