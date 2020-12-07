from flask import Blueprint, render_template

from ..models.user_models import User
from spice_status import login_manager

bp_main = Blueprint("main", __name__, url_prefix='/')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@bp_main.route('/')
def home():
    return render_template('index.html')


@bp_main.route('/raw', methods=['GET'])
def raw():
    return render_template('raw.html')
