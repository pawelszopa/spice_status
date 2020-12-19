from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired


class ProjectForm(FlaskForm):
    start_date = StringField('Project Start Date', validators=[DataRequired()])
    end_date = StringField('Project End Date', validators=[DataRequired()])
    name = StringField('Project name', validators=[DataRequired()])
    gate_1 = StringField('Gate 1 date', validators=[DataRequired()])
    gate_2 = StringField('Gate 2 date', validators=[DataRequired()])
    gate_3 = StringField('Gate 3 date', validators=[DataRequired()])
    gate_4 = StringField('Gate 4 date', validators=[DataRequired()])
    sop = StringField('Start of production date', validators=[DataRequired()])
    spice_level = StringField('Spice level', validators=[DataRequired()])
    risks = TextAreaField('Projects risks')
    low_issues = TextAreaField('Project Issues')
    high_issues = TextAreaField('Project High Issues')
    submit = SubmitField('Send')
 

class DocumentsForm(FlaskForm):
    sw_strategy = SelectField('SW-Strategy',
                              choices=[('1', 'None'), ('2', "Draft"), ('3', "In Review"), ('4', "Approved")])
    sys_strategy = SelectField('SYS-Strategy',
                               choices=[('1', 'None'), ('2', "Draft"), ('3', "In Review"), ('4', "Approved")])
    test_strategy = SelectField('Test-Strategy',
                                choices=[('1', 'None'), ('2', "Draft"), ('3', "In Review"), ('4', "Approved")])
    submit = SubmitField('Send')