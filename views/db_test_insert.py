from flask import Flask
from flask import render_template
from pymongo import MongoClient
# 블루프린트 import 꼭 하기
from views import views_template, test

client = MongoClient("mongodb+srv://test:sparta@cluster0.cpg4z.mongodb.net/Cluster0?retryWrites=true&w=majority")

app = Flask(__name__)
app.secret_key = 'sparta'

db = client.dbpokemon

a = {
    'avatar': 'default',
    'user_id': 'qwer2',
    'password': 'qwer1234',
    'phone_number': '010-2345-6789',
    'gender': '여자',
    'interest_poket': '파이리',
    'point': 5000,
    'poket_box': ['img']
}

b = {'poket_category':
    [
        '피카츄',
        '라이츄',
        '파이리',
        '꼬부기'
    ]
}

c = {
    'user_id': 'qwer1',
    'content': '작성글',
    'comment':
        [
            {
                'photo_user_id': 'qwer2',
                'photo_comment': '댓글 내용',
                'photo_avatar': '작성자 avatar'
            }
        ],
    'category': '카테고리',
    'photo': 'img',
    'desc': '글내용',
    'header': '제목',
    'date': '작성시간',
    'price': 1500
}

# db.users.insert_one(a)

# db.category.insert_one(b)

db.market.insert_one(c)