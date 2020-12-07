from flask import Blueprint, render_template, url_for
from flask_login import login_required
from werkzeug.utils import redirect

from ..forms.sample_forms import SampleForm

bp_sample = Blueprint('sample', __name__, url_prefix='/sample')


@bp_sample.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = SampleForm()
    if form.validate_on_submit():
        print('sent')
        return redirect(url_for('main.home'))

    return render_template('add.html', form=form)
