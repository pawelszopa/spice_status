from datetime import datetime

from spice_status import db


class Issue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, default=(datetime.utcnow().strftime("%m/%d/%Y")))
    description = db.Column(db.String)
    status = db.Column(db.String)
    link = db.Column(db.String, default='')
    severity = db.Column(db.String)


def get_issue_low():
    return Issue.query.filter_by(severity='Low').all()


def get_issue_mid():
    return Issue.query.filter_by(severity='Mid').all()


def get_issue_high():
    return Issue.query.filter_by(severity='High').all()


def get_issue_escalated():
    return Issue.query.filter_by(severity='Escalated').all()


def get_issue_by_id(issue_id):
    return Issue.query.filter_by(id=issue_id).first()
