import os
from moduls import write_expert_file, create_dict, write_profession_file
from reade_file.moduls import reade_file_xlsx
from db.moduls import reade_db_file

dirs = os.path.dirname("../work_file/")
file = f"{dirs}/{os.listdir(path=dirs)[0]}"
sheet = reade_file_xlsx(file)
file_not_expert = 'db\do_not_check.txt'


# if __name__ == '__main__':
    # do_not_check = reade_experts(file_not_expert)
    # experts_dict, profession_dict = create_dict(sheet, do_not_check)
    # print(write_expert_file(experts_dict))
    # print(write_profession_file(profession_dict))
