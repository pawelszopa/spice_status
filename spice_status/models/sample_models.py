from sqlalchemy import desc

from spice_status import db


class FlashCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String)
    deck = db.Column(db.String)
    front = db.Column(db.String)
    back = db.Column(db.String)

    @staticmethod
    def all_of_them():
        return FlashCard.query.order_by(desc(FlashCard.id))
