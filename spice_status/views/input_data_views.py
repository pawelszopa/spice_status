from flask import Blueprint, render_template, url_for, jsonify, flash, request
from werkzeug.utils import redirect
from .. import db
from ..forms.workbook_form import WorkBookForm
from ..models.user_models import User
from ..models.workbook_models import Workbook

bp_input = Blueprint("input", __name__, url_prefix='/metrics')


@bp_input.route('/add', methods=["GET", "POST"])
def metrics():
    form = WorkBookForm()

    if form.validate_on_submit():
        workbook = Workbook()
        form.populate_obj(workbook)
        db.session.add(workbook)
        db.session.commit()

        return redirect(url_for('main.home'))
    return render_template('data_add.html', form=form, title="Add new data")


@bp_input.route('/edit/<int:workbook_id>', methods=["GET", "POST"])
def edit(workbook_id):
    workbook = Workbook.get_metric_by_id(workbook_id)
    form = WorkBookForm(obj=workbook)

    if form.validate_on_submit():
        form.populate_obj(workbook)
        db.session.commit()
        flash(f'Saved, description: {workbook.cw}')
        return redirect(url_for('input.raw'))

    return render_template("data_add.html", form=form, title="Edit data", workbook_id=workbook_id)


@bp_input.route('/delete/<int:workbook_id>', methods=['GET', 'POST'])
def delete(workbook_id):
    workbook = Workbook.get_metric_by_id(workbook_id)

    if request.method == "POST":
        db.session.delete(workbook)
        db.session.commit()
        flash(f'Data has been removed: {workbook.cw}.')
        return redirect(url_for('input.raw'))

    else:
        flash('Please confirm deleting the bookmark.')

    return render_template("confirm_delete.html", workbook=workbook)


@bp_input.route('/raw')
def raw():
    return render_template('raw.html', raw_data=Workbook.all_of_workbooks(), users=User.all_of_users())


@bp_input.route('/charts')
def chart():
    return render_template('charts.html')


@bp_input.route('/data')
def data():
    cw = []
    shrd_total = []
    shrd_approved = []
    data = Workbook.all_of_workbooks()
    for row in data[::-1]:
        cw.append(row.cw)
    for row in data[::-1]:
        shrd_total.append(row.total_client_req)
    for row in data[::-1]:
        shrd_approved.append(row.total_client_req_approved)

    return jsonify(
        {'cw': cw,
         'shrd_total': shrd_total,
         'shrd_approved': shrd_approved})


'''
@bp_main.route('/charts', methods=['GET', "POST"])
def charts():
    shrd = []
    data = Workbook.all_of_workbooks()
    for row in data:
        shrd.append([row.cw, row.total_client_req, row.total_client_req_approved])
    shrd.insert(0, ["CW", "Total_Shrd", "Total ShRd Approved"])
    shrd = jsonify(shrd)
    data = {'Task': 'Hours per Day', 'Work': 11, 'Eat': 2, 'Commute': 2, 'Watching TV': 2, 'Sleeping': 7}
    data = [{'Task': 'Hours per Day', 'Work': 11, 'Eat': 2, 'Commute': 2, 'Watching TV': 2, 'Sleeping': 7},
            {'Work': 12, 'Eat': 4, 'Commute': 5, 'Watching TV': 8, 'Sleeping': 9}]

    return render_template('charts_google_try.html', raw_data=Workbook.all_of_workbooks(), shrd=shrd, datas=data)
'''
