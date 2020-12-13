from datetime import datetime

from sqlalchemy import desc


from spice_status import db


class Workbook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cw = db.Column(db.String, default=f'{datetime.now().isocalendar()[0]}CW{datetime.now().isocalendar()[1]}')

    total_client_req = db.Column(db.Integer)
    total_client_req_approved = db.Column(db.Integer)

    @staticmethod
    def all_of_workbooks():
        return Workbook.query.order_by(desc(Workbook.cw))
