import os
from checking_homework.moduls import write_expert_file, write_profession_file, create_dict
from reade_file.moduls import reade_file_xlsx, create_file_xls, reade_file_csv, delete_startup_file
from synopses.main import create_synopses_dict, write_synopses_file
from db.moduls import reade_experts, update_experts
from training_check.moduls import create_dict_training, create_file_treanind


def apps_run():
    folder_path = os.path.dirname("work_file/")
    file = f"{folder_path}/{os.listdir(path=folder_path)[0]}"

    request_assignment = int(input(
        'Укажите что Вы хотите сделать:'
        '\nПроверить анонсы расписания - 1; '
        '\nСделать рассылку непроверенных дз -2;'
        '\nПроверить активность тренеров -3;'
        '\nХотите проверить список доверенных экспертов -4;'
        '\nХотите провести корректировку списка доверенных экспертов - 5'
        '\nХотите проверить список экспертов которые не проверяют ДЗ -6'
        '\nХотите провести корректировку списка экспертов не проверяющих ДЗ - 7'
        '\nУкажите выбранный вариант: '))

    if request_assignment == 1:
        rez_file_synopses = 'result_file/synopses.txt'
        synopses = reade_file_csv(file)[1:]
        synopses_dict = create_synopses_dict(synopses)
        print(write_synopses_file(synopses_dict, rez_file_synopses))
    elif request_assignment == 2:
        file_not_expert = 'db/do_not_check.db'
        rez_file_expert = 'result_file/expert.txt'
        rez_file_profession = 'result_file/profession.txt'
        sheet = reade_file_xlsx(file)
        create_file_xls(file)
        do_not_check = reade_experts(file_not_expert)
        experts_dict, profession_dict = create_dict(sheet, do_not_check)
        print(write_expert_file(experts_dict, rez_file_expert))
        print(write_profession_file(profession_dict, rez_file_profession))
        print(create_file_xls(file))
    elif request_assignment == 3:
        rez_file_training = 'result_file/training.xlsx'
        sheet = reade_file_xlsx(file)
        training_dict = create_dict_training(sheet)
        print(create_file_treanind(training_dict, rez_file_training))
    elif request_assignment == 4:
        print(reade_experts('db/soft_experts.db'))
    elif request_assignment == 5:
        print(update_experts('db/soft_experts.db'))
    elif request_assignment == 6:
        print(reade_experts('db/do_not_check.db'))
    elif request_assignment == 7:
        print(update_experts('db/do_not_check.db'))

    del_request = input('Удалить файл из папки work_file Д/Н: ').lower()
    if del_request == 'д':
        delete_startup_file()