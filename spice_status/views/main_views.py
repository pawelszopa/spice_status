import json

from flask import Blueprint, render_template, jsonify

from ..models.project_models import get_project
from ..forms.issue_form import IssueForm
from ..models.issue_models import Issue, get_issue_low, get_issue_mid, get_issue_high, get_issue_escalated
from ..models.user_models import User
from spice_status import login_manager, db
from ..models.workbook_models import Workbook
from random import sample

bp_main = Blueprint("main", __name__, url_prefix='/')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@bp_main.route('/', methods=['GET', 'POST'])
def home():
    form = IssueForm()
    if form.validate_on_submit():
        issue = Issue(
            date=form.date.data,
            description=form.description.data,
            status=form.status.data,
            link='',
            severity=form.severity.data,
        )
        db.session.add(issue)
        db.session.commit()
    return render_template('status_page.html', form=form, low=get_issue_low(), mid=get_issue_mid(),
                           high=get_issue_high(), esca=get_issue_escalated(), project=get_project())


@bp_main.route('/raw')
def raw():
    return render_template('raw.html', raw_data=Workbook.all_of_workbooks(), users=User.all_of_users())


@bp_main.route('/charts', methods=['GET', "POST"])
def charts():
    shrd = []
    data = Workbook.all_of_workbooks()
    for row in data:
        shrd.append([row.cw, row.total_client_req, row.total_client_req_approved])
    shrd.insert(0, ["CW", "Total_Shrd", "Total ShRd Approved"])
    shrd = jsonify(shrd)
    data = {'Task': 'Hours per Day', 'Work': 11, 'Eat': 2, 'Commute': 2, 'Watching TV': 2, 'Sleeping': 7}
    data = [{'Task': 'Hours per Day', 'Work': 11, 'Eat': 2, 'Commute': 2, 'Watching TV': 2, 'Sleeping': 7},
            {'Work': 12, 'Eat': 4, 'Commute': 5, 'Watching TV': 8, 'Sleeping': 9}]

    return render_template('charts.html', raw_data=Workbook.all_of_workbooks(), shrd=shrd, datas=data)


@bp_main.route('/chart')
def chart():
    return render_template('chart.html')


@bp_main.route('/data')
def data():
    return jsonify({'results': sample(range(1, 10), 5), 'sss': sample(range(1, 10), 5)})
