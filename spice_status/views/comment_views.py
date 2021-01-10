from datetime import datetime

from flask import Blueprint, url_for
from werkzeug.utils import redirect

from spice_status import db
from ..models.comment_models import Comment
from ..forms.comment_forms import CommentForm

bp_comment = Blueprint("comment", __name__, url_prefix='/comments')


@bp_comment.route('/', methods=['POST'])
def comment():
    form = CommentForm()

    if form.validate_on_submit():
        comment = Comment(
            date=datetime.utcnow().strftime("%m/%d/%Y"),
            content=form.content.data,
            issue_id=form.item_id.data
        )
        db.session.add(comment)
        db.session.commit()
    return redirect(url_for('main.home', issue_id=form.issue_id.data))
# escape is cleaning text for example from SQL that shouldn't be there
