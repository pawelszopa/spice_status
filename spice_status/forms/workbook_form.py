from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired


class WorkBookForm(FlaskForm):
    total_shrd_REQ = IntegerField('total_shrd_REQ', validators=[DataRequired()])
    total_open_shrd = IntegerField('total_open_shrd', validators=[DataRequired()])
    total_sys_req = IntegerField('total_sys_req', validators=[DataRequired()])
    Total_sys_req_approved = IntegerField('Total_sys_req_approved', validators=[DataRequired()])
    submit = SubmitField('Send')
