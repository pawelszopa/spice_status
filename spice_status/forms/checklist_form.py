from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired


class Gate0Form(FlaskForm):
    date = StringField('Issue date', default=(datetime.utcnow().strftime("%m/%d/%Y")), validators=[DataRequired()])
    sw_strategy = SelectField('SW strategy created?', choices=['Yes', 'No', 'N/A'], validators=[DataRequired()])
    sys_strategy = SelectField('SyS strategy created?', choices=['Yes', 'No', 'N/A'], validators=[DataRequired()])
    test_strategy = SelectField('test strategy created?', choices=['Yes', 'No', 'N/A'], validators=[DataRequired()])
    submit = SubmitField('Submit')


class Gate1Form(Gate0Form):
    test_report = SelectField('test reports available?', choices=['Yes', 'No', 'N/A'], validators=[DataRequired()])


class Gate2Form(Gate1Form):
    test_question2 = SelectField('XYZ?', choices=['Yes', 'No', 'N/A'], validators=[DataRequired()])


class SOPForm(Gate2Form):
    is_ready = SelectField('Is device ready?', choices=['Yes', 'No', 'N/A'], validators=[DataRequired()])
