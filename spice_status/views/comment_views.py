from datetime import datetime

from flask import Blueprint, url_for, render_template
from flask_login import login_required, current_user
from werkzeug.utils import redirect, escape

from spice_status import db
from ..models.comment_models import Comment
from ..forms.comment_forms import CommentForm

bp_comment = Blueprint("comment", __name__, url_prefix='/comments')


@bp_comment.route('/', methods=['GET', 'POST'])
@login_required
def comment():
    form = CommentForm()

    if form.validate_on_submit():
        comment = Comment(
            date=datetime.utcnow().strftime("%m/%d/%Y"),
            content=escape(form.content.data),
            issue_id=form.issue_id.data,

        )
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('issue.issue', issue_id=form.issue_id.data))

# escape is cleaning text for example from SQL that shouldn't be there

