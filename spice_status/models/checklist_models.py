from datetime import datetime

from spice_status import db


class Gate0(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, default=(datetime.utcnow().strftime("%m/%d/%Y")))
    sw_strategy = db.Column(db.String)
    sys_strategy = db.Column(db.String)
    test_strategy = db.Column(db.String)


class Gate1(Gate0):
    test_report = db.Column(db.String)


class Gate2(Gate1):
    test_question2 = db.Column(db.String)


class SOP(Gate2):
    is_ready = db.Column(db.String)
