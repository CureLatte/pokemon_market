from flask import Flask
from flask import render_template
from pymongo import MongoClient


client = MongoClient("mongodb+srv://test:sparta@cluster0.cpg4z.mongodb.net/Cluster0?retryWrites=true&w=majority")

# 블루프린트 import 꼭 하기
from views import views_template, test

app = Flask(__name__)
app.secret_key = 'sparta'

db = client.dbpokemon


@app.route('/')
def main():
    return render_template('./test_page/page_0.html')


# 블루프린트 등록하는 부분 app.register_blueprint(블루프린트이름.bp)
app.register_blueprint(test.bp)
app.register_blueprint(views_template.bp)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)