from datetime import datetime

from sqlalchemy import desc

from spice_status import db


class Workbook(db.Model):
    cw = db.Column(db.String, default=f'{datetime.now().isocalendar()[0]}CW{datetime.now().isocalendar()[1]}',
                   primary_key=True)
    total_shrd_REQ = db.Column(db.Integer)
    total_open_shrd = db.Column(db.Integer)
    total_sys_req = db.Column(db.Integer)
    Total_sys_req_approved = db.Column(db.Integer)

    @staticmethod
    def all_of_workbooks():
        return Workbook.query.order_by(desc(Workbook.cw))
