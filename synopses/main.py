import os

import dateparser
from db.moduls import training_blocks
from reade_file.moduls import reade_file_csv

def modul_create(moduls):
    """
    Define the name of the key to write the announcement.
    """
    modul = moduls
    for block in training_blocks:
        if moduls in block:
            modul = block[0]
    return modul


def date_in_date(sinopsis: str) -> str:
    """
    Convert the date from the line July 13, 2023 18:00 (MSC) to the line 13.07 18.00
    """
    date_string = sinopsis[0].split(',')[0].split('(')
    date_string = date_string[0]
    date_object = dateparser.parse(date_string)
    formatted_date = date_object.strftime("%d.%m %H.%M")
    return formatted_date


def create_synopses_dict(synopses: list) -> dict:
    """
    Create a dictionary with announcements by module code from the list of announcements.
    """
    synopses_dict = {}
    for synopsis in synopses:
        if synopsis[0].split(',')[2] == 'Программирование' and synopsis[0].split(',')[1] != "" and \
                synopsis[0].split(',')[8] == 'Утверждён':
            synopsis_date = date_in_date(synopsis)
            moduls = synopsis[0].split(',')[1]
            code_produckt = moduls.split('-')[:-1][0].upper()
            code_produckt = modul_create(code_produckt)
            task = synopsis[0].split(',')[3]
            expert = synopsis[0].split(',')[4]
            synopsis_str_shot = f"{synopsis_date}  {task}  @{expert}"
            if code_produckt not in synopses_dict:
                synopses_dict[code_produckt] = {moduls: [synopsis_str_shot]}
            else:
                if moduls not in synopses_dict[code_produckt]:
                    synopses_dict[code_produckt].update({moduls: [synopsis_str_shot]})
                else:
                    synopses_dict[code_produckt][moduls] = synopses_dict[code_produckt][moduls] + [synopsis_str_shot]

    return synopses_dict

def write_synopses_file(synopses_dict: dict):
    """
    Create a file "synopses.txt" from the dictionary.
    """
    with open('../result_file/synopses.txt', 'w', encoding='utf-8') as f:
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
    return f"Создан файл {os.path.basename('../result_file/synopses.txt')}. " \
           f"В папке по адресу: {os.path.abspath('../result_file/synopses.txt')}"


if __name__ == '__main__':
    file = '../work_file/anonse.csv'
    synopses = reade_file_csv(file)[1:]
    synopses_dict = create_synopses_dict(synopses)
    print(write_synopses_file(synopses_dict))

    # for k, v in synopses_dict.items():
    #     print(k)
    #     print(':bar_chart:Всем привет. Расписание на следующую неделю:chart_with_upwards_trend:')
    #     print('')
    #
    #     for modul, synopsis in v.items():
    #         print(modul)
    #         for volue in synopsis:
    #             print(volue)
    #         print('\n')
    #     print('++++++++++++++++++')


