from flask import Blueprint, render_template, url_for

from .. import db
from ..forms.checklist_form import Gate0Form
from ..models.checklist_models import Gate0

bp_checklist = Blueprint("checklist", __name__, url_prefix='/checklist')


@bp_checklist.route('/', methods=["GET", "POST"])
def checklist_gate_1():
    form = Gate0Form()
    form.sw_strategy.data = 'None'
    form.sys_strategy.data = 'None'
    form.test_strategy.dat = 'None'
    if form.validate_on_submit():
        gate = Gate0(sw_strategy=form.sw_strategy.data,
                     sys_strategy=form.sys_strategy.data,
                     test_strategy=form.test_strategy.data)
        db.session.add(gate)
        db.session.commit()

    return render_template('checklist_gate_0.html', form=form)