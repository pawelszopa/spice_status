from flask import Blueprint, render_template, url_for
from flask_login import login_required
from werkzeug.utils import redirect

from spice_status import db
from spice_status.forms.project_forms import ProjectForm, DocumentsForm
from spice_status.models.project_models import Project, Documents

bp_project = Blueprint("project", __name__, url_prefix='/project')


@bp_project.route('/add', methods=["GET", "POST"])
@login_required
def define_new_project():
    project_form = ProjectForm()

    if project_form.validate_on_submit():
        project = Project(start_date=project_form.start_date.data,
                          end_date=project_form.end_date.data,
                          name=project_form.name.data,
                          gate_1=project_form.gate_1.data,
                          gate_2=project_form.gate_2.data,
                          gate_3=project_form.gate_3.data,

                          sop=project_form.sop.data,
                          spice_level=project_form.spice_level.data,
                          )

        db.session.add(project)
        db.session.commit()
        return redirect(url_for('main.home'))

    return render_template("create_new_project.html", form=project_form)



