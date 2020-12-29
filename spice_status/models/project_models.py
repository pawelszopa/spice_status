from spice_status import db


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.String)
    end_date = db.Column(db.String)
    name = db.Column(db.String)
    gate_1 = db.Column(db.String)
    gate_2 = db.Column(db.String)
    gate_3 = db.Column(db.String)
    sop = db.Column(db.String)
    spice_level = db.Column(db.String)
    risks = db.Column(db.String)
    low_issues = db.Column(db.String)
    high_issues = db.Column(db.String)


class Documents(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sw_strategy = db.Column(db.String)
    sys_strategy = db.Column(db.String)
    test_strategy = db.Column(db.String)


def get_project():
    return Project.query.first()



