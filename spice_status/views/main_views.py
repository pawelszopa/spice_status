from flask import Blueprint, render_template, flash

from ..models.project_models import get_project
from ..forms.issue_form import IssueForm, FilterForm
from ..models.issue_models import Issue, get_all_issues
from ..models.user_models import User
from spice_status import login_manager, db

bp_main = Blueprint("main", __name__, url_prefix='/')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@bp_main.route('/', methods=['GET', 'POST'])
def home():


    issue_form = IssueForm()
    filter_form = FilterForm()

    if issue_form.submit.data and issue_form.validate_on_submit():
        issue = Issue(
            date=issue_form.date.data,
            title=issue_form.title.data,
            description=issue_form.description.data,
            status=issue_form.status.data,
            severity=issue_form.severity.data,
            spice_process=issue_form.spice_process.data,
            link='',
        )
        db.session.add(issue)
        db.session.commit()
        flash(f"Item {Issue.id} has been successfully added", "success")

    issues = Issue.query.all()

    if filter_form.submit.data and filter_form.validate_on_submit():

        if filter_form.title.data:
            issues_temp = []
            for issue in issues:
                if filter_form.title.data in issue.title:
                    issues_temp.append(issue)
            issues = issues_temp

        if filter_form.description.data:
            issues_temp = []
            for issue in issues:
                if filter_form.description.data in issue.description:
                    issues_temp.append(issue)
            issues = issues_temp

        if filter_form.status.data != 'NA':
            issues_temp = []
            for issue in issues:
                if filter_form.status.data in issue.status:
                    issues_temp.append(issue)
            issues = issues_temp

        if filter_form.severity.data != 'NA':
            issues_temp = []
            for issue in issues:
                if filter_form.severity.data in issue.severity:
                    issues_temp.append(issue)
            issues = issues_temp

        # if filter_form.spice_process.data == 'NA':
        #     issues_temp = []
        #     for issue in issues:
        #         if filter_form.spice_process.data in issue.spice_process:
        #             issues_temp.append(issue)
        #     issues = issues_temp




    return render_template('status_page.html', issue_form=issue_form, issues=issues, project=get_project(),
                           filter_form=filter_form)
