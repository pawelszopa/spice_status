from flask import Blueprint, flash, url_for, render_template, request
from flask_login import login_required
from werkzeug.utils import redirect

from ..models.comment_models import Comment
from .. import db
from ..forms.issue_form import EditIssueForm
from ..forms.comment_forms import CommentForm
from ..models.issue_models import get_issue_by_id, Issue

bp_issue = Blueprint("issue", __name__, url_prefix='/issue')


@bp_issue.route('/<int:issue_id>')
@login_required
def issue(issue_id):
    issue = Issue.query.filter_by(id=issue_id).first()
    comment_form = CommentForm()
    comment_form.issue_id.data = issue_id
    comments = Comment.query.filter_by(issue_id=issue_id).all()

    return render_template('issue.html', issue=issue, CommentForm=comment_form, comments=comments)


@bp_issue.route('/edit/<int:issue_id>', methods=["GET", "POST"])
@login_required
def edit(issue_id):
    db_item = get_issue_by_id(issue_id)
    if db_item:
        form = EditIssueForm(obj=db_item)

        if form.validate_on_submit():
            form.populate_obj(db_item)
            db.session.commit()
            flash(f"Item {issue_id} has been successfully modified", "success")
            return redirect(url_for('main.home'))
        return render_template('edit_item.html', issue=db_item, form=form, issue_id=issue_id)
    else:
        return render_template('404.html')


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
