from datetime import datetime

from spice_status import db


class Issue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, default=str(datetime.utcnow()))
    description = db.Column(db.String)
    status = db.Column(db.String)
    link = db.Column(db.String, default='')
    severity = db.Column(db.String)

def get_issue_low():
    return Issue.query.filter_by(severity='Low').all()

