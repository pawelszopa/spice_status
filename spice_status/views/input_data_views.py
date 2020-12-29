from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect
from .. import db
from ..forms.workbook_form import WorkBookForm
from ..models.workbook_models import Workbook

bp_input = Blueprint("input", __name__, url_prefix='/metrics')


@bp_input.route('/', methods=["GET", "POST"])
def metrics():
    form = WorkBookForm()

    if form.validate_on_submit():

        workbook = Workbook(cw=form.cw.data, total_client_req=form.total_client_req.data,
                            total_client_req_approved=form.total_client_req_approved.data)
        db.session.add(workbook)
        db.session.commit()

        return redirect(url_for('main.home'))
    return render_template('data_add.html', form=form)

