from flask import Blueprint

bp_checklist = Blueprint("checklist", __name__, url_prefix='/checklist')


@bp_checklist.route('/', methods=["GET", "POST"])
def checklist_gate_1():
    
    return True
