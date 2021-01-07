from flask import Blueprint, render_template, flash

from ..models.project_models import get_project
from ..forms.issue_form import IssueForm
from ..models.issue_models import Issue, get_all_issues
from ..models.user_models import User
from spice_status import login_manager, db

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
    return render_template('status_page.html', form=form, issues=Issue.query.all(), project=get_project())
