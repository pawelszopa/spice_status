from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length


class IssueForm(FlaskForm):
    date = StringField('Issue date', validators=[DataRequired()])
    description = StringField('Description', validators=[Length(min=15), DataRequired()])
    status = SelectField('Status', choices=['New', 'Assign', 'WIP', 'In Review', 'Closed'],
                         validators=[DataRequired()])
    link = StringField('link')
    severity = SelectField('Severity', choices=['Low', 'Mid', 'High', 'Escalated', 'Escalated', 'Escalated'],
                           validators=[DataRequired()])
    submit = SubmitField("Create")
