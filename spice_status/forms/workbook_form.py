from datetime import datetime

from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import IntegerField, SubmitField, StringField, FloatField, FileField
from wtforms.validators import InputRequired, DataRequired


class WorkBookForm(FlaskForm):
    cw = StringField('Calendar Week leave empty to set current', default=f'{datetime.utcnow().strftime("%m/%d/%Y")}')
    total_client_req = IntegerField('total_client_req', validators=[DataRequired()])
    total_client_req_approved = IntegerField('total_client_req_approved', validators=[InputRequired()])
    total_open_issue_client_req = IntegerField('total_open_issue_client_req', validators=[InputRequired()])
    total_sys_req = IntegerField('total_sys_req', validators=[InputRequired()])
    total_sys_req_approved = IntegerField('total_sys_req_approved', validators=[InputRequired()])
    total_sys_req_implemented = IntegerField('total_sys_req_implemented', validators=[InputRequired()])
    total_sw_req = IntegerField('total_sw_req', validators=[InputRequired()])
    total_sw_req_approved = IntegerField('total_sw_req_approved', validators=[InputRequired()])
    total_sw_req_implemented = IntegerField('total_sw_req_implemented', validators=[InputRequired()])
    ccm_more_50 = IntegerField('ccm_more_50', validators=[InputRequired()])
    ccm_24_50 = IntegerField('ccm_24_50', validators=[InputRequired()])
    ccm_12_24 = IntegerField('ccm_12_24', validators=[InputRequired()])
    misra_high = IntegerField('misra_high', validators=[InputRequired()])
    misra_mid = IntegerField('misra_mid', validators=[InputRequired()])
    misra_low = IntegerField('misra_low', validators=[InputRequired()])
    branch_coverage = FloatField('branch_coverage', validators=[InputRequired()])
    line_coverage = FloatField('line_coverage', validators=[InputRequired()])
    mc_dc_coverage = FloatField('mc_dc_coverage', validators=[InputRequired()])
    total_sw_req_tests = IntegerField('total_sw_req_tests', validators=[InputRequired()])
    total_sw_req_passed = IntegerField('total_sw_req_passed', validators=[InputRequired()])
    total_sys_req_tests = IntegerField('total_sys_req_tests', validators=[InputRequired()])
    total_sys_req_tests_passed = IntegerField('total_sys_req_tests_passed', validators=[InputRequired()])
    traceability_sys_client = IntegerField('traceability_sys_client', validators=[InputRequired()])
    traceability_client_sys = IntegerField('traceability_client_sys', validators=[InputRequired()])
    traceability_sys_sw = IntegerField('traceability_sys_sw', validators=[InputRequired()])
    traceability_sw_sys = IntegerField('traceability_sw_sys', validators=[InputRequired()])
    total_features = IntegerField('total_features', validators=[InputRequired()])
    total_bugs = IntegerField('total_bugs', validators=[InputRequired()])
    total_bugs_solved = IntegerField('total_bugs_solved', validators=[InputRequired()])
    total_problems = IntegerField('total_problems', validators=[InputRequired()])
    total_problems_solved = IntegerField('total_problems_solved', validators=[InputRequired()])
    total_change_requests = IntegerField('total_change_requests', validators=[InputRequired()])
    change_request_not_reviewed = IntegerField('change_request_not_reviewed', validators=[InputRequired()])
    submit = SubmitField('Send')


class ExcelForm(FlaskForm):
    excel = FileField('Excel File')
    id_min = IntegerField('Min ID number', validators=[DataRequired(), InputRequired()])
    id_max = IntegerField('Max ID number', validators=[DataRequired(), InputRequired()])
    submit = SubmitField('ADD')
