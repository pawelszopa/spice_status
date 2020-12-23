from spice_status import db
from spice_status.models.workbook_models import Workbook


def get_db_shrd():
    data = db
    print(data)
    return True


get_db_shrd()
