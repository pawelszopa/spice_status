from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired


class Gate0Form(FlaskForm):
    date = StringField('Gate Date', default=(datetime.utcnow().strftime("%m/%d/%Y")))
    sw_strategy = SelectField('SW strategy created?', choices=['Not set', 'Yes', 'No', 'N/A'], validators=[DataRequired()])
    sys_strategy = SelectField('SyS strategy created?', choices=['Not set', 'Yes', 'No', 'N/A'], validators=[DataRequired()])
    test_strategy = SelectField('test strategy created?', choices=['Not set', 'Yes', 'No', 'N/A'], validators=[DataRequired()])
    submit = SubmitField('Submit')


class Gate1Form(Gate0Form):
    test_report = SelectField('test reports available?', choices=['Not set', 'Yes', 'No', 'N/A'], validators=[DataRequired()])


class Gate2Form(Gate1Form):
    test_question2 = SelectField('XYZ?', choices=['Not set', 'Yes', 'No', 'N/A'], validators=[DataRequired()])


class SOPForm(Gate2Form):
    is_ready = SelectField('Is device ready?', choices=['Not set', 'Yes', 'No', 'N/A'], validators=[DataRequired()])
