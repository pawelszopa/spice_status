from datetime import datetime

from sqlalchemy import desc


from spice_status import db


class Workbook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cw = db.Column(db.String)

    total_client_req = db.Column(db.Integer)
    total_client_req_approved = db.Column(db.Integer)

    total_open_issue_client_req = db.Column(db.Integer)
    total_sys_req = db.Column(db.Integer)
    total_sys_req_approved = db.Column(db.Integer)
    total_sys_req_implemented = db.Column(db.Integer)
    total_sw_req = db.Column(db.Integer)
    total_sw_req_approved = db.Column(db.Integer)
    total_sw_req_implemented = db.Column(db.Integer)
    ccm_more_50 = db.Column(db.Integer)
    ccm_24_50 = db.Column(db.Integer)
    ccm_12_24 = db.Column(db.Integer)
    misra_high = db.Column(db.Integer)
    misra_mid = db.Column(db.Integer)
    misra_low = db.Column(db.Integer)
    branch_coverage = db.Column(db.Float)
    line_coverage = db.Column(db.Float)
    mc_dc_coverage = db.Column(db.Float)
    total_sw_req_tests = db.Column(db.Integer)
    total_sw_req_passed = db.Column(db.Integer)
    total_sys_req_tests = db.Column(db.Integer)
    total_sys_req_tests_passed = db.Column(db.Integer)
    traceability_sys_client = db.Column(db.Integer)
    traceability_client_sys = db.Column(db.Integer)
    traceability_sys_sw = db.Column(db.Integer)
    traceability_sw_sys = db.Column(db.Integer)
    total_features = db.Column(db.Integer)
    total_bugs = db.Column(db.Integer)
    total_bugs_solved = db.Column(db.Integer)
    total_problems = db.Column(db.Integer)
    total_problems_solved = db.Column(db.Integer)
    total_change_requests = db.Column(db.Integer)
    change_request_not_reviewed = db.Column(db.Integer)

    @staticmethod
    def all_of_workbooks():
        return Workbook.query.order_by(desc(Workbook.cw))

    @staticmethod
    def workbook_query():
        return Workbook.query.all()

    @staticmethod
    def get_metric_by_id(idx):
        return Workbook.query.get_or_404(idx)