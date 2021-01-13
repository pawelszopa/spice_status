from flask import Blueprint, render_template
from flask_login import login_required

from ..models.issue_models import Issue
from ..models.checklist_models import Gate0, Gate1, Gate2, SOP
from ..models.project_models import Project

from ..models.user_models import User
from spice_status import login_manager

bp_main = Blueprint("main", __name__, url_prefix='/')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@bp_main.route('/', methods=['GET'])
@login_required
def home():
    if Gate0.query.order_by(Gate0.id.desc()).first():
        gate0 = Gate0.query.order_by(Gate0.id.desc()).first()
        gate0_values = gate0.__dict__.values()
        g0_status = 'Green'
        if 'No' in gate0_values:
            g0_status = 'Red'

    if Gate1.query.order_by(Gate1.id.desc()).first():
        gate1 = Gate1.query.order_by(Gate1.id.desc()).first()
        gate1_values = gate1.__dict__.values()
        g1_status = 'Green'
        if 'No' in gate1_values:
            g1_status = 'Red'

    if Gate2.query.order_by(Gate2.id.desc()).first():
        gate2 = Gate2.query.order_by(Gate2.id.desc()).first()
        gate2_values = gate2.__dict__.values()
        g2_status = 'Green'
        if 'No' in gate2_values:
            g2_status = 'Red'

    if SOP.query.order_by(SOP.id.desc()).first():
        sop = SOP.query.order_by(SOP.id.desc()).first()
        sop_values = sop.__dict__.values()
        sop_status = 'Green'
        if 'No' in sop_values:
            sop_status = 'Red'

    issues = Issue.query.all()
    sys1 = 0
    for issue in issues:
        print(issue.spice_process)
        if issue.severity in ['Escalated', "High"] and issue.spice_process == 'SYS.1':
            sys1 += 1
    if sys1 > 0:
        sys_1 = 'fail'
    else:
        sys_1 = 'pass'

    sys2 = 0
    for issue in issues:
        print(issue.spice_process)
        if issue.severity in ['Escalated', "High"] and issue.spice_process == 'SYS.2':
            sys2 += 1
    if sys1 > 0:
        sys_2 = 'fail'
    else:
        sys_2 = 'pass'

    sys3 = 0
    for issue in issues:
        print(issue.spice_process)
        if issue.severity in ['Escalated', "High"] and issue.spice_process == 'SYS.3':
            sys1 += 1
    if sys3 > 0:
        sys_3 = 'fail'
    else:
        sys_3 = 'pass'

    sys4 = 0
    for issue in issues:
        print(issue.spice_process)
        if issue.severity in ['Escalated', "High"] and issue.spice_process == 'SYS.4':
            sys4 += 1
    if sys4 > 0:
        sys_4 = 'fail'
    else:
        sys_4 = 'pass'

    sys5 = 0
    for issue in issues:
        print(issue.spice_process)
        if issue.severity in ['Escalated', "High"] and issue.spice_process == 'SYS.5':
            sys5 += 1
    if sys5 > 0:
        sys_5 = 'fail'
    else:
        sys_5 = 'pass'

    swe1 = 0
    for issue in issues:
        print(issue.spice_process)
        if issue.severity in ['Escalated', "High"] and issue.spice_process == 'SWE.1':
            swe1 += 1
    if swe1 > 0:
        swe_1 = 'fail'
    else:
        swe_1 = 'pass'

    swe2 = 0
    for issue in issues:
        print(issue.spice_process)
        if issue.severity in ['Escalated', "High"] and issue.spice_process == 'SWE.2':
            swe2 += 1
    if swe2 > 0:
        swe_2 = 'fail'
    else:
        swe_2 = 'pass'

    swe3 = 0
    for issue in issues:
        print(issue.spice_process)
        if issue.severity in ['Escalated', "High"] and issue.spice_process == 'SWE.3':
            swe3 += 1
    if swe3 > 0:
        swe_3 = 'fail'
    else:
        swe_3 = 'pass'

    swe4 = 0
    for issue in issues:
        print(issue.spice_process)
        if issue.severity in ['Escalated', "High"] and issue.spice_process == 'SWE.4':
            swe4 += 1
    if swe4 > 0:
        swe_4 = 'fail'
    else:
        swe_4 = 'pass'

    swe5 = 0
    for issue in issues:
        print(issue.spice_process)
        if issue.severity in ['Escalated', "High"] and issue.spice_process == 'SWE.5':
            swe5 += 1
    if swe5 > 0:
        swe_5 = 'fail'
    else:
        swe_5 = 'pass'

    swe6 = 0
    for issue in issues:
        print(issue.spice_process)
        if issue.severity in ['Escalated', "High"] and issue.spice_process == 'SWE.6':
            swe6 += 1
    if swe6 > 0:
        swe_6 = 'fail'
    else:
        swe_6 = 'pass'

    sup1 = 0
    for issue in issues:
        print(issue.spice_process)
        if issue.severity in ['Escalated', "High"] and issue.spice_process == 'SUP.1':
            sup1 += 1
    if sup1 > 0:
        sup_1 = 'fail'
    else:
        sup_1 = 'pass'

    sup8 = 0
    for issue in issues:
        print(issue.spice_process)
        if issue.severity in ['Escalated', "High"] and issue.spice_process == 'SUP.8':
            sup8 += 1
    if sup8 > 0:
        sup_8 = 'fail'
    else:
        sup_8 = 'pass'

    sup9 = 0
    for issue in issues:
        print(issue.spice_process)
        if issue.severity in ['Escalated', "High"] and issue.spice_process == 'SUP.9':
            sup9 += 1
    if sup9 > 0:
        sup_9 = 'fail'
    else:
        sup_9 = 'pass'

    sup10 = 0
    for issue in issues:
        print(issue.spice_process)
        if issue.severity in ['Escalated', "High"] and issue.spice_process == 'SUP.10':
            sup10 += 1
    if sup10 > 0:
        sup_10 = 'fail'
    else:
        sup_10 = 'pass'

    man3 = 0
    for issue in issues:
        print(issue.spice_process)
        if issue.severity in ['Escalated', "High"] and issue.spice_process == 'MAN.3':
            man3 += 1
    if man3 > 0:
        man_3 = 'fail'
    else:
        man_3 = 'pass'

    man5 = 0
    for issue in issues:
        print(issue.spice_process)
        if issue.severity in ['Escalated', "High"] and issue.spice_process == 'MAN.5':
            man5 += 1
    if man5 > 3:
        man_5 = 'fail'
    else:
        man_5 = 'pass'

    return render_template('status_page.html',
                           project=Project.get_project(),
                           gate0_values=gate0_values,
                           g0_status=g0_status,
                           g1_status=g1_status,
                           g2_status=g2_status,
                           sop_status=sop_status,
                           sys_1=sys_1,
                           sys_2=sys_2,
                           sys_3=sys_3,
                           sys_4=sys_4,
                           sys_5=sys_5,
                           swe_1=swe_1,
                           swe_2=swe_2,
                           swe_3=swe_3,
                           swe_4=swe_4,
                           swe_5=swe_5,
                           swe_6=swe_6,
                           sup_1=sup_1,
                           sup_8=sup_8,
                           sup_9=sup_9,
                           sup_10=sup_10,
                           man_3=man_3,
                           man_5=man_5,
                           )
