from flask import Blueprint
from flask import request
from flask import jsonify
from flask import redirect, url_for, render_template
from flask import Flask

bp = Blueprint("profile", __name__, url_prefix='/profile')
app = Flask(__name__)
app.secret_key = 'sparta'


@bp.route('/home', methods=['GET'])
def open_profile():
    test = {'name': 'bobboy', 'point': 3000, 'my_box':[1,2,3,4]}

    return render_template('jinja_guide.html', container=test)
