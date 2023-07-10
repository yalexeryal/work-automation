import openpyxl
from datetime import datetime
import os


def create_dict_training(sheet) -> dict:
    treining_dict: dict = {}
    for row in sheet.iter_rows(min_row=2, values_only=True):
        treining = row[9]
        date_check = datetime.strptime(row[10], "%d.%m.%Y").date()

        if treining in treining_dict:
            if treining_dict[treining] < date_check:
                treining_dict[treining] = date_check
        else:
            treining_dict[treining] = date_check
    return treining_dict


def create_file_treanind(treining_dict: dict, rez_file_treining):
    wb = openpyxl.Workbook()
    list = wb.active
    # Создание строки с заголовками
    list.append(('Тренер', 'Дата'))
    for i, j in treining_dict.items():
        a = (i, j)
        list.append(a)

    wb.save(rez_file_treining)
    return f"Создан файл {os.path.basename(rez_file_treining)}. В папке по адресу: {os.path.abspath(rez_file_treining)}"
