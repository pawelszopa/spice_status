from flask import Blueprint, render_template
from flask_login import login_required

from ..models.checklist_models import Gate0, Gate1, Gate2, SOP
from ..models.project_models import Project

from ..models.user_models import User
from spice_status import login_manager

bp_main = Blueprint("main", __name__, url_prefix='/')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@bp_main.route('/', methods=['GET'])
@login_required
def home():
    if Gate0.query.order_by(Gate0.id.desc()).first():
        gate0 = Gate0.query.order_by(Gate0.id.desc()).first()
        gate0_values = gate0.__dict__.values()
        g0_status = 'Green'
        if 'No' in gate0_values:
            g0_status = 'Red'

    if Gate1.query.order_by(Gate1.id.desc()).first():
        gate1 = Gate1.query.order_by(Gate1.id.desc()).first()
        gate1_values = gate1.__dict__.values()
        g1_status = 'Green'
        if 'No' in gate1_values:
            g1_status = 'Red'

    if Gate2.query.order_by(Gate2.id.desc()).first():
        gate2 = Gate2.query.order_by(Gate2.id.desc()).first()
        gate2_values = gate2.__dict__.values()
        g2_status = 'Green'
        if 'No' in gate1_values:
            g2_status = 'Red'

    if SOP.query.order_by(SOP.id.desc()).first():
        sop = SOP.query.order_by(SOP.id.desc()).first()
        sop_values = sop.__dict__.values()
        sop_status = 'Green'
        if 'No' in sop_values:
            sop_status = 'Red'

    return render_template('status_page.html', project=Project.get_project(), gate0_values=gate0_values,
                           g0_status=g0_status, g1_status=g1_status, g2_status=g2_status, sop_status=sop_status)
