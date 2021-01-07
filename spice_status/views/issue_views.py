from flask import Blueprint, flash, url_for, render_template
from werkzeug.utils import redirect

from .. import db
from ..forms.issue_form import EditIssueForm
from ..models.issue_models import get_issue_by_id

bp_issue = Blueprint("issue", __name__, url_prefix='/issue')


@bp_issue.route('/edit/<int:issue_id>', methods=["GET", "POST"])
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