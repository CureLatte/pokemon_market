from flask import Flask
from pymongo import MongoClient
import uuid
import datetime


client = MongoClient("mongodb+srv://test:sparta@cluster0.cpg4z.mongodb.net/Cluster0?retryWrites=true&w=majority")

app = Flask(__name__)
app.secret_key = 'sparta'

db = client.dbpokemon

# a = {
#     'avatar': 'default',
#     'user_id': 'qwer2',
#     'password': 'qwer1234',
#     'phone_number': '010-2345-6789',
#     'gender': '여자',
#     'interest_poket': '파이리',
#     'point': 5000,
#     'poket_box': ['img']
# }
#
# b = {'poket_category':
#     [
#         '피카츄',
#         '라이츄',
#         '파이리',
#         '꼬부기'
#     ]
# }

i = uuid.uuid1()
today = datetime.datetime.now()
today_time = today.strftime('%Y-%m-%d %OH:%OM:%OS')

c = {
    'maket_id': str(i),
    'user_id': 'qwer1',
    'content': '작성글2',
    'comment':
        [
            {
                'photo_user_id': 'qwer3',
                'photo_comment': '안녕하세요',
                'photo_avatar': '작성자 avata3r'
            },
{
                'photo_user_id': 'qwer1',
                'photo_comment': '댓글 입니다',
                'photo_avatar': '작성자 avatar1'
            },
{
                'photo_user_id': 'qwer2',
                'photo_comment': '그렇쿤요',
                'photo_avatar': '작성자 avatar2'
            },
            {
                'photo_user_id': 'qwer4',
                'photo_comment': '아 네',
                'photo_avatar': '작성자 avatar4'
            }
        ],
    'category': '카테고리',
    'photo': 'img',
    'desc': '청도 프리미엄 특 왕 반건시 VIP 감동 선물세트',
    'header': '제목2',
    'date': today_time,
    'price': 1500
}

# db.users.insert_one(a)

# db.category.insert_one(b)

db.market.insert_one(c)