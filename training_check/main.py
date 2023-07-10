from moduls import create_dict, create_file
from reade_file.moduls import reade_file_xlsx

sheet = reade_file_xlsx(0)

if __name__ == '__main__':
    rez_file_treining = '../result_file/traning.xlsx'
    treining_dict = create_dict(sheet)
    print(create_file(treining_dict, rez_file_treining))
