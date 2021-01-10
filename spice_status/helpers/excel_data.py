import os
from openpyxl import load_workbook


def excel_data(id_min, id_max, row_range=35):
    filename = os.path.join(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'uploads'), 'excel.xlsx')
    wb = load_workbook(filename)
    ws = wb.active
    id_range = [f'id{idx}' for idx in range(id_min, id_max + 1)]
    cords = []


    for idx in id_range:
        for col in ws.iter_rows():
            for cell in col:
                if cell.value == idx:
                    cw_field = cell.coordinate
                    cords.append(cw_field)

    print(cords)
    cords_letters = []
    for item in cords:
        for _ in item:
            if not _.isdigit():
                cord_letter = _
                cords_letters.append(cord_letter)

    final_data = []
    for letter in cords_letters:
        data = []
        for digit in range(2, row_range + 1):
            cell = f'{letter}{digit}'
            data.append(ws[cell].value)
        final_data.append(data)

    return final_data
