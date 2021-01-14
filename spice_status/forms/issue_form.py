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
    spice_process = SelectField('Process',
                                choices=['SYS.1', 'SYS.2', 'SYS.3', 'SYS.4', 'SYS.5', 'SWE.1', 'SWE.2', 'SWE.3',
                                         'SWE.4', 'SWE.5', 'SWE.6', 'SUP.1', 'SUP.8', 'SUP.9', 'SUP.10', 'MAN.3',
                                         'MAN.5'],
                                validators=[DataRequired()])
    submit = SubmitField("Create")


class EditIssueForm(FlaskForm):
    title = StringField('Title', validators=[Length(min=1, max=64, message='Title must be up to 64')])
    description = StringField('Description', validators=[Length(min=15), DataRequired()])
    link = StringField('link')
    status = SelectField('Status', choices=['New', 'Assign', 'WIP', 'In Review', 'Closed'],
                         validators=[DataRequired()])
    severity = SelectField('Severity', choices=['Low', 'Mid', 'High', 'Escalated'],
                           validators=[InputRequired()])
    spice_process = SelectField('Process',
                                choices=['SYS.1', 'SYS.2', 'SYS.3', 'SYS.4', 'SYS.5', 'SWE.1', 'SWE.2', 'SWE.3',
                                         'SWE.4', 'SWE.5', 'SWE.6', 'SUP.1', 'SUP.8', 'SUP.9', 'SUP.10', 'MAN.3',
                                         'MAN.5'],
                                validators=[DataRequired()])
    submit = SubmitField("Edit")


class FilterForm(FlaskForm):
    title = StringField('Title', validators=[Length(max=10, message='Max 10')])
    description = StringField('Description', validators=[Length(max=15)])
    status = SelectField('Status', choices=['New', 'Assign', 'WIP', 'In Review', 'Closed', 'NA'], default='NA')
    severity = SelectField('Severity', choices=['Low', 'Mid', 'High', 'Escalated', 'NA'], default='NA')
    spice_process = SelectField('Process', choices=['SYS.1', 'SYS.2', 'SYS.3', 'SYS.4', 'SYS.5', 'SWE.1',
                                                    'SWE.2', 'SWE.3',
                                                    'SWE.4', 'SWE.5', 'SWE.6', 'SUP.1', 'SUP.8', 'SUP.9',
                                                    'SUP.10', 'MAN.3',
                                                    'MAN.5','NA'], default='NA')
    submit = SubmitField("Filter")
