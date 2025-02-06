import os
from openpyxl import Workbook

from reade_file.moduls import reade_file_xlsx
from db.start_models import models


def sorted_dict(unsorted_dictionary: dict) -> dict:
    sorted_tuple = sorted(unsorted_dictionary.items(), key=lambda x: x[0])
    return dict(sorted_tuple)


def create_channels_dict(channels: list) -> dict:
    """
    Creating Dictionaries
    channels_dict - list for creating channels
    """

    channels_dict = {}

    for row in channels.iter_rows(min_row=2, values_only=True):
        model_split = (row[1].split('-')[:-1])
        model_join = '-'.join(model_split).lower()

        if model_join in models:
            if model_join not in channels_dict:
                channels_dict[model_join] = (row[1], row[6], row[2])

    return sorted_dict(channels_dict)


def write_channels_file(channels_dict: dict, name_file: str):
    workbook = Workbook()

    sheet = workbook.active

    header = ['Код модуля', 'Дата', 'Координатор']
    sheet.append(header)

    for channel in channels_dict.values():
        values = channel
        sheet.append(values)
    # workbook.save('channels_data.xlsx')

    workbook.save(name_file)
    return f"Создан файл {os.path.basename(name_file)}. В папке по адресу: {os.path.abspath(name_file)}"


if __name__ == '__main__':
    dirs = os.path.dirname("../work_file/")
    file = f"{dirs}/{os.listdir(path=dirs)[0]}"
    name_file = 'Заполнение_LMS'
    channels = reade_file_xlsx(file)
    channels_dict = create_channels_dict(channels)
    write_channels_file(channels_dict, name_file)
