from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField


class SampleForm(FlaskForm):
    type = SelectField('Type', choices=[('1', 'Basic'), ('2', "Advanced")])
    deck = StringField('Deck')
    front = StringField("Front")
    back = StringField("Back")
    submit = SubmitField('Add')