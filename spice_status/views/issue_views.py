from flask import Blueprint, flash, url_for, render_template, request
from werkzeug.utils import redirect

from .. import db
from ..forms.issue_form import EditIssueForm
from ..models.issue_models import get_issue_by_id, Issue

bp_issue = Blueprint("issue", __name__, url_prefix='/issue')


@bp_issue.route('/edit/<int:issue_id>', methods=["GET", "POST"])
def edit(issue_id):
    db_item = get_issue_by_id(issue_id)
    form = EditIssueForm(obj=db_item)

    if form.validate_on_submit():
        form.populate_obj(db_item)
        db.session.commit()
        flash(f"Item {issue_id} has been successfully modified", "success")
        return redirect(url_for('main.home'))
    return render_template('edit_item.html', issue=db_item, form=form, issue_id=issue_id)


@bp_issue.route('/delete/<int:issue_id>', methods=["GET", "POST"])
def delete(issue_id):
    db_item = Issue.query.filter_by(id=issue_id).first()
    if request.method == "POST":
        db.session.delete(db_item)
        db.session.commit()
        flash(f'Data has been removed: {db_item.description}.')
        return redirect(url_for('main.home'))

    else:
        flash('Please confirm deleting the issue.')

    return render_template("confirm_delete.html", issue_id=issue_id, issue=db_item)
