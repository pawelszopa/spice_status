from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, InputRequired


class IssueForm(FlaskForm):
    date = StringField('Issue date', default=(datetime.utcnow().strftime("%m/%d/%Y")), validators=[DataRequired()])
    description = StringField('Description', validators=[Length(min=15), DataRequired()])
    status = SelectField('Status', choices=['New', 'Assign', 'WIP', 'In Review', 'Closed'],
                         validators=[DataRequired()])
    link = StringField('link')
    severity = SelectField('Severity', choices=['Low', 'Mid', 'High', 'Escalated'],
                           validators=[DataRequired()])
    submit = SubmitField("Create")


class EditIssueForm(FlaskForm):
    description = StringField('Description', validators=[Length(min=15), DataRequired()])
    link = StringField('link')
    status = SelectField('Status', choices=['New', 'Assign', 'WIP', 'In Review', 'Closed'],
                         validators=[DataRequired()])
    severity = SelectField('Severity', choices=['Low', 'Mid', 'High', 'Escalated'],
                           validators=[InputRequired()])
    submit = SubmitField("Edit")
