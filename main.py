import os
import openpyxl
from reade_file.moduls import reade_file_xlsx, create_file_xls

if __name__ == '__main__':
    dirs = os.path.dirname("work_file/")
    file = f"{dirs}/{os.listdir(path=dirs)[0]}"
    sheet = reade_file_xlsx(file)
    create_file_xls(sheet)


