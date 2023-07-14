import os
from moduls import create_dict, write_expert_file

from reade_file.moduls import reade_file_xlsx
from db.moduls import reade_db_file

# dirs = os.path.dirname("../work_file/")
# file = f"{dirs}/{os.listdir(path=dirs)[0]}"
# sheet = reade_file_xlsx(file)
# trusted_expert_coursework = '../db//trusted_expert_coursework.db'

if __name__ == '__main__':
   dirs = os.path.dirname("../work_file/")
   file = f"{dirs}/{os.listdir(path=dirs)[0]}"
   sheet = reade_file_xlsx(file)
   trusted_expert_coursework = '../db//trusted_expert_coursework.db'
   trusted_expert_coursework = reade_db_file(trusted_expert_coursework)
   diploma_blocks = '../db/diploma_blocks.db'
   result_file = '../result_file/expert_dip.txt'
   expert_dict = create_dict(sheet, diploma_blocks)
   write_expert_file(expert_dict, result_file, trusted_expert_coursework)
