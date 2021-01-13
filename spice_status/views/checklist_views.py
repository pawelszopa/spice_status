from flask import Blueprint, render_template, url_for, flash
from flask_login import login_required
from werkzeug.utils import redirect

from .. import db
from ..forms.checklist_form import Gate0Form, Gate1Form, Gate2Form, SOPForm
from ..models.checklist_models import Gate0, Gate1, Gate2, SOP

bp_checklist = Blueprint("checklist", __name__, url_prefix='/checklist')


@bp_checklist.route('/gate0', methods=["GET", "POST"])
@login_required
def checklist_gate_0():
    form = Gate0Form()

    if form.validate_on_submit():
        if form.test_strategy.data == 'Not set' or form.sys_strategy.data == 'Not set' or form.sw_strategy.data == 'Not set':
            flash('You have to set data', 'danger')
            return redirect(url_for('checklist.checklist_gate_0'))
        gate = Gate0(sw_strategy=form.sw_strategy.data,
                     sys_strategy=form.sys_strategy.data,
                     test_strategy=form.test_strategy.data)
        db.session.add(gate)
        db.session.commit()
        flash('Subbmited', 'success')
        return redirect(url_for('main.home'))

    return render_template('checklist_gate_0.html', form=form)


@bp_checklist.route('/gate1', methods=["GET", "POST"])
@login_required
def checklist_gate_1():
    form = Gate1Form()

    if form.validate_on_submit():
        if form.test_report.data == 'Not set' or \
                form.test_strategy.data == 'Not set' or \
                form.sys_strategy.data == 'Not set' or \
                form.sw_strategy.data == 'Not set':
            flash('You have to set data', 'danger')
            return redirect(url_for('checklist.checklist_gate_1'))
        gate = Gate1(sw_strategy=form.sw_strategy.data,
                     sys_strategy=form.sys_strategy.data,
                     test_strategy=form.test_strategy.data,
                     test_report=form.test_report.data)
        db.session.add(gate)
        db.session.commit()

        flash('Subbmited', 'success')
        return redirect(url_for('main.home'))

    return render_template('checklist_gate_0.html', form=form)


@bp_checklist.route('/gate2', methods=["GET", "POST"])
@login_required
def checklist_gate_2():
    form = Gate2Form()

    if form.validate_on_submit():
        if form.test_report.data == 'Not set' or \
                form.test_strategy.data == 'Not set' or \
                form.sys_strategy.data == 'Not set' or \
                form.sw_strategy.data == 'Not set' or \
                form.test_question2.data == 'Not set':
            flash('You have to set data', 'danger')
            return redirect(url_for('checklist.checklist_gate_2'))
        gate = Gate2(sw_strategy=form.sw_strategy.data,
                     sys_strategy=form.sys_strategy.data,
                     test_strategy=form.test_strategy.data,
                     test_report=form.test_report.data,
                     test_question2=form.test_question2.data)
        db.session.add(gate)
        db.session.commit()
        flash('Subbmited', 'success')
        return redirect(url_for('main.home'))

    return render_template('checklist_gate_0.html', form=form)


@bp_checklist.route('/sop', methods=["GET", "POST"])
@login_required
def checklist_gate_sop():
    form = SOPForm()

    if form.validate_on_submit():
        if form.test_report.data == 'Not set' or \
                form.test_strategy.data == 'Not set' or \
                form.sys_strategy.data == 'Not set' or \
                form.sw_strategy.data == 'Not set' or \
                form.test_question2.data == 'Not set' or \
                form.is_ready.data == 'Not set':
            flash('You have to set data', 'danger')
            return redirect(url_for('checklist.checklist_gate_sop'))

        gate = SOP(sw_strategy=form.sw_strategy.data,
                   sys_strategy=form.sys_strategy.data,
                   test_strategy=form.test_strategy.data,
                   test_report=form.test_report.data,
                   test_question2=form.test_question2.data,
                   is_ready=form.is_ready.data)
        db.session.add(gate)
        db.session.commit()
        flash('Subbmited', 'success')
        return redirect(url_for('main.home'))

    return render_template('checklist_gate_0.html', form=form)
