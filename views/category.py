from static.model.poketmon_class import poket_all_class
from flask import Blueprint, redirect, url_for, jsonify, request, render_template
from pymongo import MongoClient
from static.model.poketmon_class import poket_all_class


client = MongoClient("mongodb+srv://test:sparta@cluster0.cpg4z.mongodb.net/Cluster0?retryWrites=true&w=majority")

sorted_data = sorted(poket_all_class.items(), key=lambda x: x[1])

bp = Blueprint('category', __name__, url_prefix='/category')


@bp.route('/')
def load_category():
    BASE_CODE = 44032
    CHOSUNG = 588
    category_sort = sorted(poket_all_class.items(), key=lambda x: x[1])
    category_korean = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
    dict_by_letter = {}
    for index, poketmon_name in category_sort:
        string_list = list(poketmon_name)
        first_letter_index = int((ord(string_list[0]) - BASE_CODE) / CHOSUNG)
        if category_korean[first_letter_index] not in dict_by_letter:
            dict_by_letter[category_korean[first_letter_index]] = [poketmon_name]
        else:
            list_by_letter = dict_by_letter[category_korean[first_letter_index]]
            list_by_letter.append(poketmon_name)
    return render_template('base.html', container=dict_by_letter, koreans=category_korean)

