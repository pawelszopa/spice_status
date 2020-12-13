from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, StringField
from wtforms.validators import InputRequired


class WorkBookForm(FlaskForm):
    cw = StringField('Calendar Week leave empty to set current',
                     default=f'{datetime.now().isocalendar()[0]}CW{datetime.now().isocalendar()[1]}')
    total_client_req = IntegerField('total_client_req', validators=[InputRequired()])
    total_client_req_approved = IntegerField('total_client_req_approved', validators=[InputRequired()])
    submit = SubmitField('Send')
