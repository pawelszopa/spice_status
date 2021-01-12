import os
from datetime import datetime

from flask import Blueprint, render_template, url_for, jsonify, flash, request
from flask_login import login_required
from werkzeug.utils import redirect
from .. import db
from ..forms.workbook_form import WorkBookForm, ExcelForm

from ..models.user_models import User
from ..models.workbook_models import Workbook
from ..helpers import excel_data

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


@bp_input.route('/add/excel', methods=['GET', 'POST'])
@login_required
def excel():
    form = ExcelForm()
    if form.validate_on_submit():
        form.excel.data.save(
            os.path.join(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'uploads'), 'excel.xlsx'))

        excel_values = excel_data(form.id_min.data, form.id_max.data)

        for item in excel_values:

            if item[0] is None:
                item[0] = f'{datetime.utcnow().strftime("%m/%d/%Y")}'

            workbook = Workbook(
                cw=item[0],
                total_client_req=item[1],
                total_client_req_approved=item[2],
                total_open_issue_client_req=item[3],
                total_sys_req=item[4],
                total_sys_req_approved=item[5],
                total_sys_req_implemented=item[6],
                total_sw_req=item[7],
                total_sw_req_approved=item[8],
                total_sw_req_implemented=item[9],
                ccm_more_50=item[10],
                ccm_24_50=item[11],
                ccm_12_24=item[12],
                misra_high=item[13],
                misra_mid=item[14],
                misra_low=item[15],
                branch_coverage=item[16],
                line_coverage=item[17],
                mc_dc_coverage=item[18],
                total_sw_req_tests=item[19],
                total_sw_req_passed=item[20],
                total_sys_req_tests=item[21],
                total_sys_req_tests_passed=item[22],
                traceability_sys_client=item[23],
                traceability_client_sys=item[24],
                traceability_sys_sw=item[25],
                traceability_sw_sys=item[26],
                total_features=item[27],
                total_bugs=item[28],
                total_bugs_solved=item[29],
                total_problems=item[30],
                total_problems_solved=item[31],
                total_change_requests=item[32],
                change_request_not_reviewed=item[33],
            )
            db.session.add(workbook)
            db.session.commit()
            flash(f'Data id: {item[0]} has been added', 'success')
        return redirect(url_for('input.raw'))

    return render_template('add_data_excel.html', form=form)


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
