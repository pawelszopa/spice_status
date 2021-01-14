from functools import wraps

from flask import flash, url_for, render_template, Blueprint
from flask.views import View
from flask_login import current_user, login_required
from werkzeug.utils import redirect

from ..models.comment_models import Comment
from ..models.issue_models import Issue
from ..models.checklist_models import SOP, Gate2, Gate1, Gate0
from ..models.workbook_models import Workbook
from ..models.project_models import Project
from ..models.user_models import User

bp_admin = Blueprint('admin', __name__, template_folder='templates')


def admin_required(fn):
    @wraps(fn)
    def _admin_required(*args, **kwargs):
        if not current_user.is_admin:
            flash('You need to be administrator to access this page', 'danger')
            return redirect(url_for('auth.login'))
        return fn(*args, **kwargs)

    return _admin_required


class AdminView(View):
    decorators = [admin_required, login_required]

    def dispatch_request(self):
        return render_template('admin_view.html')


class TableView(View):
    decorators = [admin_required, login_required]

    def __init__(self, model, edit_allowed=False):
        self.edit_allowed = edit_allowed
        self.model = model
        self.columns = self.model.__mapper__.columns.keys()
        self.resource_name = self.model.__name__.lower()
        super(TableView, self).__init__()

    def dispatch_request(self):
        return render_template('resource_table.html', columns=self.columns, instances=self.model.query.all(),
                               edit_allowed=True, resource_name=self.resource_name)


bp_admin.add_url_rule('/users', view_func=TableView.as_view('user', model=User))
bp_admin.add_url_rule('/projects', view_func=TableView.as_view('project', model=Project))
bp_admin.add_url_rule('/workbooks', view_func=TableView.as_view('workbook', model=Workbook))
bp_admin.add_url_rule('/checklists0', view_func=TableView.as_view('checklist0', model=Gate0))
bp_admin.add_url_rule('/checklists1', view_func=TableView.as_view('checklist1', model=Gate1))
bp_admin.add_url_rule('/checklists2', view_func=TableView.as_view('checklist2', model=Gate2))
bp_admin.add_url_rule('/checklistsSOP', view_func=TableView.as_view('checklistSOP', model=SOP))
bp_admin.add_url_rule('/comments', view_func=TableView.as_view('comment', model=Comment))
bp_admin.add_url_rule('/issues', view_func=TableView.as_view('issue', model=Issue))
bp_admin.add_url_rule('/', view_func=AdminView.as_view('admin'))
