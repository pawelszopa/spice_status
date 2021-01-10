from datetime import datetime

from spice_status import db


class Issue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, default=(datetime.utcnow().strftime("%m/%d/%Y")))
    title = db.Column(db.String)
    description = db.Column(db.String)
    status = db.Column(db.String)
    severity = db.Column(db.String)
    spice_process = db.Column(db.String)
    link = db.Column(db.String, default='')
    # comments = db.relationship("Comment", backref='Issue', lazy='dynamic')

def get_all_issues():
    return Issue.query.all()


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
