from flask import Blueprint, render_template

from forms.issue_form import IssueForm
from models.issue_models import Issue
from ..models.user_models import User
from spice_status import login_manager, db
from ..models.workbook_models import Workbook

bp_main = Blueprint("main", __name__, url_prefix='/')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@bp_main.route('/')
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
    return render_template('status_page.html', form=form)


@bp_main.route('/raw')
def raw():
    return render_template('raw.html', raw_data=Workbook.all_of_workbooks(), users=User.all_of_users())
