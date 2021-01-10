from datetime import datetime

from spice_status import db


class Comment(db.Model):
    item_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, default=(datetime.utcnow().strftime("%m/%d/%Y")))
    content = db.Column(db.String(256))
    # issue_id = db.Column(db.Integer, db.ForeignKey('issue.id'), nullable=False)
