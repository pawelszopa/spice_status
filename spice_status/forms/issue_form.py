from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, InputRequired


class IssueForm(FlaskForm):
    date = StringField('Issue date', default=(datetime.utcnow().strftime("%m/%d/%Y")), validators=[DataRequired()])
    title = StringField('Title', validators=[Length(min=1, max=64, message='Title must be up to 64')])
    description = StringField('Description', validators=[Length(min=15), DataRequired()])
    status = SelectField('Status', choices=['New', 'Assign', 'WIP', 'In Review', 'Closed'],
                         validators=[DataRequired()])
    link = StringField('link')
    severity = SelectField('Severity', choices=['Low', 'Mid', 'High', 'Escalated'],
                           validators=[DataRequired()])
    spice_process = SelectField('Process', choices=['SyS', 'SW', 'SUP', 'MAN'],
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


class FilterForm(FlaskForm):
    title = StringField('Title', validators=[Length(max=10, message='Max 10')])
    description = StringField('Description', validators=[Length(max=15)])
    status = SelectField('Status', choices=['New', 'Assign', 'WIP', 'In Review', 'Closed', 'NA'], default='NA')
    severity = SelectField('Severity', choices=['Low', 'Mid', 'High', 'Escalated', 'NA'], default='NA')
    spice_process = SelectField('Process', choices=['SyS', 'SW', 'SUP', 'MAN', 'NA'], default='NA')
    submit = SubmitField("Filter")
