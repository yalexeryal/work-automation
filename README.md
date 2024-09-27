# work automation
## checking_homework
**Выборка непроверенных ДЗ.**

1. Резместить в дериктории work_files файл с расширением xlsx(в директории должен быть только один файл).
2. Результат выборке находится в директории result_files.
    * файл "experts.txt" выборка работ по проверяющим экспертам.
    * файл "profession.txt" выборка работ с не закрепленными проверяющими экспертами.
    * файл "Непроверенные работы (дата).xlsx" отредактированный файл для выгрузки координаторам.

## checking_homework
**Выборка непроверенных курсовых и дипломов.**

1. Резместить в дериктории work_files файл с расширением xlsx(в директории должен быть только один файл).
2. Результат выборке находится в директории result_files.
    * файл "coursework.txt" выборка работ по проверяющим экспертам.
    * файл "Непроверенные дипломы (дата).xlsx" отредактированный файл для выгрузки координаторам.


## training_check
**Проверка тренеров.**

1. Резместить в дериктории work_files файл с расширением xlsx (в директории должен быть только один файл).
2. Результат выборки по последней дате проверке тренером в файле "training.xlsx" в директории result_files.

## synopses
**Выбор анонсов расписания вебинаров на неделю.**

1. Резместить в дериктории work_files файл с расширением csv (в директории должен быть только один файл).
2. Результат выборка анонсов расписаний по модулям обучения в файле "synopses.txt" в директории result_files.


## creating_channels
**Выбор модулей для создания каналов**
1. Разместить в директории work_files файл с расширением xlsx (в директории должен быть только один файл).
2. Результат выборки по последней дате проверке тренером в файле "channels.xlsx" в директории result_files.


## db
**Редактирование баз экспертов, файлы находятся в папке db.**

1. Доверенные эксперты, эксперты не допускающие просрочек проверки ДЗ - "soft_experts.db".
2. Эксперты, которые перестали проверять ДЗ "do_not_check.db".
3. Доверенные эксперты, эксперты не допускающие просрочек проверки курсовых - "trusted_expert_coursework.db".
4. Дипломные блоки - "diploma_blocks.db"
