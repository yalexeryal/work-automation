import csv
import os
import datetime
import openpyxl

def reade_file_xlsx(file, num=0):
    """
    Reads xlsx file
    """
    wb = openpyxl.load_workbook(file, data_only=True)
    sheet = wb.active
    return sheet


def create_file_xls(sheet_list: list):
    todys = datetime.datetime.today().date()
    wb = openpyxl.Workbook()
    sheet = wb.active

    sheet.append(('БЮ', 'Код продукта', 'Код набора', 'Название задания', 'id задания', 'Ссылка на работу',
                  'Ссылка на работу в новом ЛК', 'Студент', 'Дедлайн', 'Дедлайн пользователя', 'Дата отправки',
                  'Проверяющий', 'Возможные проверяющие', 'Дней на проверке'))
    for product in sheet.iter_rows(min_row=2, values_only=True):
        product = [product[0], product[1].upper(), product[2], product[5], product[4], product[12], product[13],
                   product[8], product[7], product[7], product[9], product[10], product[11], int(product[14])]
        sheet.append(product)
    wb.save(f"result_file/Непроверенные работы {todys}.xlsx")


def reade_file_csv(file: csv):
    with open(file, encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        anonse_list = list(reader)
        return anonse_list

def delete_startup_file():
    """
    Delete the original data file from the work_file folder.
    """
    folder_path = os.path.dirname("work_file/")
    file_list = os.listdir(folder_path)
    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)


if __name__ == '__main__':
    dir_name = "../result_file/"
    dirs = os.path.dirname("../work_file/")
    file = f"{dirs}/{os.listdir(path=dirs)[0]}"
    sheet = reade_file_xlsx(file)
    create_file_xls(sheet, dir_name)
