import os
import datetime
from db.moduls import training_blocks, reade_db_file

file_soft_expert = 'db/soft_experts.db'
soft_expert = reade_db_file(file_soft_expert)


def get_weekday_days_inspections() -> tuple:
    """
    Get the names of the day of the week and the dates of overdue homework, check today and tomorrow.
    """
    day_name = datetime.date.today().strftime("%A")
    today = datetime.date.today()

    answer = input('Вы хотите сами установить даты проверки? Если да то нажмите -1')
    if answer == '1':
        overdue = datetime.datetime.strptime(input('Ведите дату просрочки в формате 1999-12-24: '), "%Y-%m-%d").date()
        tomorrow_start = datetime.datetime.strptime(
            input('Ведите дату первого дня проверки на завтра в формате 1999-12-24: '), "%Y-%m-%d").date()
        tomorrow_finish = datetime.datetime.strptime(
            input('Ведите дату второго дня проверки на завтра в формате 1999-12-24: '), "%Y-%m-%d").date()
        return day_name, overdue, tomorrow_start, tomorrow_finish

    else:
        if day_name == 'Monday' or day_name == 'Tuesday':
            overdue = today - datetime.timedelta(days=6)
            tomorrow_start = today - datetime.timedelta(days=4)
            tomorrow_finish = today - datetime.timedelta(days=4)
            return day_name, overdue, tomorrow_start, tomorrow_finish

        elif day_name == 'Wednesday':
            overdue = today - datetime.timedelta(days=6)
            tomorrow_start = today - datetime.timedelta(days=2)
            tomorrow_finish = today - datetime.timedelta(days=2)
            return day_name, overdue, tomorrow_start, tomorrow_finish

        elif day_name == 'Thursday' or day_name == 'Friday':
            overdue = today - datetime.timedelta(days=4)
            tomorrow_start = today - datetime.timedelta(days=2)
            tomorrow_finish = today - datetime.timedelta(days=2)
            return day_name, overdue, tomorrow_start, tomorrow_finish


def checker_inspector(checker: list | str, inspectors: list) -> str:
    """
    Bringing out the checker.
    """
    if checker is not None:
        return checker
    elif len(inspectors) == 1 and inspectors is not None:
        return str(inspectors[0])


def check_inspector(profession_experts: set, soft_expert: set, overdue, submitted) -> bool:
    new_profession_experts = profession_experts.issubset(soft_expert)
    if submitted <= overdue or new_profession_experts == False:
        return True
    else:
        return False


def message_template(day_name: str) -> tuple:
    if day_name == 'Friday':
        new_list_expert = ['Привет!',
                           ['Есть просроченные ДЗ необходимо проверить в ближайшее время:\n'],
                           ['\nСегодня до конца дня необходимо проверить ДЗ:\n'],
                           ['\nНа всякий случай - до понедельника до конца дня необходимо проверить ДЗ:\n'],
                           ]
        new_list_profession = ['Коллеги, всем добрый день!',
                               ['Есть просроченные ДЗ, необходимо проверить в ближайшее время:\n'],
                               ['\nСегодня до конца дня необходимо проверить ДЗ:\n'],
                               [
                                   '\nНа всякий случай напоминаю, что до понедельника до конца дня необходимо '
                                   'проверить ДЗ:\n'],
                               set()
                               ]
        return new_list_expert, new_list_profession
    else:
        new_list_expert = ['Привет!',
                           ['Есть просроченные ДЗ необходимо проверить в ближайшее время:\n'],
                           ['\nСегодня до конца дня необходимо проверить ДЗ:\n'],
                           ['\nНа всякий случай - до завтра до конца дня необходимо проверить ДЗ:\n'],
                           ]
        new_list_profession = ['Коллеги, всем добрый день!',
                               ['Есть просроченные ДЗ, необходимо проверить в ближайшее время:\n'],
                               ['\nСегодня до конца дня необходимо проверить ДЗ:\n'],
                               ['\nНа всякий случай напоминаю, что до завтра до конца дня необходимо проверить ДЗ:\n'],
                               set()
                               ]
        return new_list_expert, new_list_profession


def date_filter(overdue: datetime, tomorrow_start: datetime, submitted: datetime, row: tuple) -> tuple:
    """
    Enter dates and a row from the works list, give the list index to add and a row to output.

    """
    overdue_date = overdue
    tomorrow_start_date = tomorrow_start
    modul = row[2]
    session = row[3]
    session_link = row[12]
    student = row[8]

    if submitted <= overdue_date:
        return 1, f"{modul}    {session}    {session_link}    {student}    {submitted}"

    elif overdue_date < submitted < tomorrow_start_date:
        return 2, f"{modul}    {session}    {session_link}    {student}"

    elif tomorrow_start_date <= submitted:
        return 3, f"{modul}    {session}    {session_link}    {student}"


def write_expert_file(experts_dict: dict, rez_file_expert) -> str:
    """
    Write data from the "experts_dict" dictionary into the file
    """
    with open(rez_file_expert, 'w', encoding='utf-8') as f:
        for ex_d in experts_dict.items():
            if ex_d[0] in soft_expert:
                if len(ex_d[1][1]) > 1:
                    name_exp = f"\n\n {ex_d[0]}  \nПривет!\n"
                    f.write(name_exp)
                    for hw in ex_d[1][1]:
                        rez = f"{hw}\n"
                        f.write(rez)
            else:
                name_exp = f"\n\n {ex_d[0]}  \nПривет!\n"
                f.write(name_exp)
                if len(ex_d[1][1]) > 1:
                    for hw in ex_d[1][1]:
                        rez = f"{hw}\n"
                        f.write(rez)
                if len(ex_d[1][2]) > 1:
                    for hw in ex_d[1][2]:
                        rez = f"{hw}\n"
                        f.write(rez)
                if len(ex_d[1][3]) > 1:
                    for hw in ex_d[1][3]:
                        rez = f"{hw}\n"
                        f.write(rez)
    return f"Создан файл {os.path.basename(rez_file_expert)}. " \
           f"В папке по адресу: {os.path.abspath(rez_file_expert)}"


def write_profession_file(profession_dict: dict, rez_file_profession) -> str:
    """
    Write data from the "profession_dict" dictionary into the file
    """
    with open(rez_file_profession, 'w', encoding='utf-8') as f:
        for prof_d in profession_dict.items():
            modul = f"\n\n {prof_d[0]}  \n:house_with_garden: Коллеги, всем добрый день!:house_with_garden:\n"
            f.write(modul)
            if len(prof_d[1][1]) > 1:
                for hw in prof_d[1][1]:
                    rez = f"{hw}\n"
                    f.write(rez)
            if len(prof_d[1][2]) > 1:
                for hw in prof_d[1][2]:
                    rez = f"{hw}\n"
                    f.write(rez)
            if len(prof_d[1][3]) > 1:
                for hw in prof_d[1][3]:
                    rez = f"{hw}\n"
                    f.write(rez)
            rez = '@' + " @".join(sorted(list(prof_d[1][4])))
            f.write(rez)
    return f"Создан файл {os.path.basename(rez_file_profession)}. " \
           f"В папке по адресу: {os.path.abspath(rez_file_profession)}"


def modul_create(moduls):
    modul = moduls
    for block in training_blocks:
        if moduls in block:
            modul = block[0]
    return modul


def sorted_dict(unsorted_dictionary: dict) -> dict:
    sorted_tuple = sorted(unsorted_dictionary.items(), key=lambda x: x[0])
    return dict(sorted_tuple)


def create_dict(sheet, do_not_check) -> tuple:
    """
    Creating Dictionaries
    experts_dict - unverified tasks with assigned experts
    profession_dict - untested tasks not assigned to experts
    """

    experts_dict = {}
    profession_dict = {}
    day_name, overdue, tomorrow_start, tomorrow_finish = get_weekday_days_inspections()
    new_list_expert, new_list_profession = message_template(day_name)

    for row in sheet.iter_rows(min_row=2, values_only=True):
        submitted = datetime.datetime.strptime(row[9], "%Y-%m-%d").date()
        if submitted <= tomorrow_finish:
            moduls = row[1].upper()
            checker = row[10]
            inspectors = set(str(row[11]).split(', '))
            inspectors.difference_update(do_not_check)
            inspectors = list(inspectors)
            checker = checker_inspector(checker, inspectors)
            profession_experts = set(inspectors)
            outcome = date_filter(overdue, tomorrow_start, submitted, row)
            ind, rez = outcome[0], outcome[1]

            if checker is not None or len(inspectors) == 1:
                checker = checker_inspector(checker, inspectors)
                outcome = date_filter(overdue, tomorrow_start, submitted, row)
                ind, rez = outcome[0], outcome[1]

                if checker not in experts_dict:
                    experts_dict[checker] = new_list_expert.copy()
                    experts_dict[checker][ind] = experts_dict[checker][ind] + [rez]

                else:
                    experts_dict[checker][ind] = experts_dict[checker][ind] + [rez]

            else:
                modul = modul_create(moduls)
                flag = check_inspector(profession_experts, soft_expert, overdue, submitted)
                if flag:
                    if modul not in profession_dict:
                        profession_dict[modul] = new_list_profession.copy()
                        profession_dict[modul][ind] = profession_dict[modul][ind] + [rez]
                        profession_dict[modul][4] = profession_dict[modul][4].union(profession_experts)
                    else:
                        profession_dict[modul][ind] = profession_dict[modul][ind] + [rez]
                        profession_dict[modul][4] = profession_dict[modul][4].union(profession_experts)

    print(
        f"День недели: - {day_name}\n Просрочено: по - {overdue}\n Проверить до завтра: -{tomorrow_start} - {tomorrow_finish}")
    return sorted_dict(experts_dict), sorted_dict(profession_dict)
