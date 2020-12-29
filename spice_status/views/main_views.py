import json

from flask import Blueprint, render_template, jsonify, url_for, flash
from werkzeug.utils import redirect

from ..models.project_models import get_project
from ..forms.issue_form import IssueForm, EditIssueForm
from ..models.issue_models import Issue, get_issue_low, get_issue_mid, get_issue_high, get_issue_escalated, \
    get_issue_by_id
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
        flash(f"Item {Issue.id} has been successfully added", "success")
    return render_template('status_page.html', form=form, low=get_issue_low(), mid=get_issue_mid(),
                           high=get_issue_high(), esca=get_issue_escalated(), project=get_project())


@bp_main.route('/edit/<int:issue_id>', methods=["GET", "POST"])
def edit(issue_id):
    db_item = get_issue_by_id(issue_id)
    form = EditIssueForm()
    form.status.data = db_item.status
    form.severity.data = db_item.severity
    form.description.data = db_item.description
    form.link.data = db_item.link
    if form.validate_on_submit():
        db_item.status = form.status.data
        db_item.severity = form.status.data
        db_item.description = form.status.data
        db_item.link = form.status.data
        db.session.commit()
        flash(f"Item {issue_id} has been successfully modified", "success")
        return redirect(url_for('main.home'))
    return render_template('edit_item.html', issue=db_item, form=form)


@bp_main.route('/raw')
def raw():
    return render_template('raw.html', raw_data=Workbook.all_of_workbooks(), users=User.all_of_users())


'''
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

    return render_template('charts_google_try.html', raw_data=Workbook.all_of_workbooks(), shrd=shrd, datas=data)
'''


@bp_main.route('/charts')
def chart():
    return render_template('charts.html')


@bp_main.route('/data')
def data():
    cw = []
    shrd_total = []
    shrd_approved = []
    data = Workbook.all_of_workbooks()
    for row in data[::-1]:
        cw.append(row.cw)
    for row in data:
        shrd_total.append(row.total_client_req)
    for row in data:
        shrd_approved.append(row.total_client_req_approved)

    return jsonify(
        {'cw': cw,
         'shrd_total': shrd_total,
         'shrd_approved': shrd_approved})



