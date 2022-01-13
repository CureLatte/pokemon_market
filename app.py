from flask import Flask
from flask import render_template
from pymongo import MongoClient
# 작성해야하는 부분
from views import model_test, category



client = MongoClient("mongodb+srv://test:sparta@cluster0.cpg4z.mongodb.net/Cluster0?retryWrites=true&w=majority")

# 블루프린트 import 꼭 하기

app = Flask(__name__)
app.secret_key = 'sparta'

db = client.dbpokemon

# 블루프린트 등록하는 부분 app.register_blueprint(파일이름.bp)
app.register_blueprint(model_test.bp)
app.register_blueprint(category.bp)


@app.route('/')
def main():
    return render_template('base.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)