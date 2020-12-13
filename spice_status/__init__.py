import os

from flask import Flask

from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
login_manager = LoginManager()

base_dir = os.path.abspath(os.path.dirname(__file__))


def create_app():
    spice_status = Flask(__name__)

    spice_status.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{os.path.join(base_dir, "spice_status.db")}'
    spice_status.config["SECRET_KEY"] = b'\x18\xff`\x18T\xe7\x88\xb7\xbdh\x163\xe1\x823\x85'

    from .views import bp_main

    from .views import bp_auth
    from .views.input_data_views import bp_input
    spice_status.register_blueprint(bp_main)

    spice_status.register_blueprint(bp_auth)
    spice_status.register_blueprint(bp_input)
    db.init_app(spice_status)
    Migrate(spice_status, db)

    login_manager.session_protection = 'strong'
    login_manager.login_view = 'auth.login'
    login_manager.init_app(spice_status)

    return spice_status
