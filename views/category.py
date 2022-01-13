from static.model.poketmon_class import poket_all_class
from flask import Blueprint, redirect, url_for, jsonify, request, render_template
from pymongo import MongoClient

client = MongoClient("mongodb+srv://test:sparta@cluster0.cpg4z.mongodb.net/Cluster0?retryWrites=true&w=majority")

sorted_data = sorted(poket_all_class.items(), key=lambda x: x[1])

bp = Blueprint('category',__name__,url_prefix='/category')


@bp.route('/')
def load_category():

    return render_template('base.html')

