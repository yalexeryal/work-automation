import datetime
import os
import dateparser
from db.moduls import training_blocks
from reade_file.moduls import reade_file_csv


def sorted_dict(unsorted_dictionary: dict):
    sorted_tuple = sorted(unsorted_dictionary.items(), key=lambda x: x[0])
    return dict(sorted_tuple)


def modul_create(moduls):
    """
    Define the name of the key to write the announcement.
    """
    modul = moduls
    for block in training_blocks:
        if moduls in block:
            modul = block[0]
    return modul


def date_in_date(synopsis: str) -> str:
    """
    Convert the date from the line July 13, 2023 18:00 (MSC) to the line 13.07 18.00
    """
    date_string = synopsis[0].split(',')[0].split('(')
    date_string = date_string[0]
    date_object = dateparser.parse(date_string)
    formatted_date = date_object.strftime("%d.%m %H.%M")
    return formatted_date


def create_synopses_dict(synopses: list) -> dict:
    """
    Create a dictionary with announcements by module code from the list of announcements.
    """
    header = synopses.pop(0)
    synopses_dict = {}
    for synopsis in synopses:
        flag_syn = "Утверждён" in synopsis[8]
        if synopsis[2] == 'Программирование' and flag_syn:
            synopsis_date = date_in_date(synopsis[0])
            moduls = synopsis[1]
            moduls = moduls.upper()
            code_produckt = moduls.rsplit('-', maxsplit=1)[0].upper()
            code_produckt = modul_create(code_produckt).upper()
            task = synopsis[3]
            expert = synopsis[4]
            synopsis_str_shot = f"{synopsis_date}  {task}  @{expert} \n"
            if code_produckt not in synopses_dict:
                synopses_dict[code_produckt] = {moduls.upper(): [synopsis_str_shot]}
            else:
                if moduls not in synopses_dict[code_produckt]:
                    synopses_dict[code_produckt].update({moduls.upper(): [synopsis_str_shot]})
                else:
                    synopses_dict[code_produckt][moduls].extend(synopsis_str_shot)  # Добавляем данные в список
        else:
            print(synopsis[8], synopsis[2], synopsis[0], synopsis[1])


    return sorted_dict(synopses_dict)


def write_synopses_file(synopses_dict: dict, file):
    """
    Create a file "synopses.txt" from the dictionary.
    """
    with open(file, 'w', encoding='utf-8') as f:
        for k, v in synopses_dict.items():
            f.write('\n\n')
            f.write(k)
            f.write('\n')
            f.write(':bar_chart:Всем привет. Расписание на следующую неделю:chart_with_upwards_trend:')
            f.write('\n')
            for modul, synopsis in v.items():
                f.write('\n')
                f.write(modul)
                f.write('\n')
                for volue in synopsis:
                    f.write(volue)
                f.write('\n')
            f.write('--------')
    return f"Создан файл {os.path.basename(file)}. " \
           f"В папке по адресу: {os.path.abspath(file)}"


if __name__ == '__main__':
    dirs = os.path.dirname("../work_file/")
    file = f"{dirs}/{os.listdir(path=dirs)[0]}"
    synopses = reade_file_csv(file)[1:]
    synopses_dict = create_synopses_dict(synopses)
    write_synopses_file(synopses_dict, file)
