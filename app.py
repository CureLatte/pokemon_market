from flask import Flask
from flask import render_template
from pymongo import MongoClient
from views import views_template, test

client = MongoClient("mongodb+srv://<id>:<password>>@cluster0.kgq1f.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

app = Flask(__name__)
app.secret_key = 'sparta'

db = client.test


@app.route('/')
def main():  # put application's code here

    return render_template('./test_page/page_0.html')


app.register_blueprint(test.bp)
app.register_blueprint(views_template.bp)
# app.register_blueprint(auth.bp)
# app.register_blueprint(post.bp)
# app.register_blueprint(mypage.bp)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)