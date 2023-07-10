training_blocks = [
    ['JAVA', 'JM'],
    ['BTRX', 'BWEB', 'BPATTI', 'BPATTC', 'BCONT', 'BBAY', 'FBTRX'],
    ['CPP', 'info-cpp', 'CPPS', 'CPPM', 'ALGOCPP', 'CPPL', 'SQLCPP', 'MAP', 'DPCPP', 'QT', 'IOT', 'PUE', 'FCPP'],
    ['DEVOPS', 'info-devops', 'MNT', 'DevKub', 'CloKub', 'GIT-DEV', 'VIRTD', 'TER', 'KONF', 'CICD-Dev', 'MON-DEV',
     'MICROS', 'KUBER', 'CLOPRO', 'FDEVOPS'],
    ['PY', 'PYAPI', 'SQLPY'],
    ['FPY', 'FPYMQ', 'FPYJS', 'FPYAJS', 'FPYAHJ', 'FFPY'],
    ['IOS', 'info-ios', 'BIOS', 'IBALGO', 'AIOS', 'IOSUI', 'IOSINT', 'IOSDT', 'IOSADV', 'FIOS'],
    ['NDJS', 'info-ndjs', 'NDSE', 'NDTNF', 'FNDJS'],
    ['NTW', 'info-ntw', 'BNTW', 'RUTSW', 'RSNT', 'DRUT', 'SECNT', 'WFNT', 'QOS', 'CRPNT', 'OPTNT', 'IPNT', 'FNTW'],
    ['ONEC', 'SRK', 'BALGO', 'VY', 'INF', 'SID', 'REGIS', 'FILE', 'RNFD', 'IND', 'MA', 'PV', 'BPZ', 'DTK', 'BSP',
     'OCEDT', 'TAT', 'MROC', 'OCPS'],
    ['PAE', 'PBAS', 'PWIN', 'PNET', 'SCADA', 'PHD', 'CODEPLC', 'PIB', 'PMS'],
    ['QAMID', 'FAQA', 'JSQA', 'JSAQA', 'MQA', 'LOADQA', 'IBQA'],
    ['SIB', 'INFOSIB', 'IBB', 'IBNET', 'IBGIT', 'IBOS', 'IBDEV', 'IBWEB', 'IBDEF', 'IBMOD', 'IBINC'],
    ['SQLD', 'SQLSLIN', 'SQLBASH', 'DWH-SQLD', 'SQLSDB', 'SQLDB'],
    ['SYS', 'SRLB', 'SDB', 'SLINA', 'SLINB', 'SLINC', 'NET', 'BASH', 'SVIRT', 'CICD', 'SMON', 'SFLT', 'SYSDB', 'SDBSQL',
     'SYSSEC', 'SLINA-LINUX', 'NET-LINUX', 'COURSE-FOPS', 'GIT-FOPS', 'BD-DEV']
]


# def create_experts(list_experts, file):
#     """
#     Initial loading from a pre-compiled list
#     """
#     with open(file, 'w', encoding='UTF-8') as nc:
#         for i in list_experts:
#             nc.write(f"{i}\n")
# #
# create_experts(soft_experts, 'soft_experts.txt')

def reade_experts(file):
    with open(file, 'r', encoding='UTF-8') as nc:
        experts_file = nc.read()
        expert = set(experts_file.split('\n'))
        return expert


def update_experts(file):
    experts = reade_experts(file)
    expert = ''
    while expert != 'q':
        expert = input('Ведите Имя и Фамилию эксперта: ')
        if expert == "q":
            continue
        else:
            experts.add(expert)
    write_experts(file, experts)
    return experts


def del_experts(experts, expert):
    experts.discard(expert)
    return experts


def write_experts(file, experts):
    with open(file, 'w', encoding='UTF-8') as nc:
        for i in experts:
            nc.write(f"{i}\n")


# soft_experts = reade_experts('soft_experts.db')
# print(soft_experts)
#
# print('Дияз Сейфетдинов' in soft_experts)
# soft_experts.add('Дияз Сейфетдинов')
# print('Дияз Сейфетдинов' in soft_experts)
# print(update_experts('soft_experts.txt', soft_experts))

if __name__ == "__mane__":
    do_not_check = reade_experts('do_not_check.db')
    soft_experts = reade_experts('soft_experts.db')
    print(update_experts(soft_experts))
    # do_not_check = update_experts(do_not_check, 'Aktrcfylh Zqkj[fyjd')
    # write_experts('do_not_check.txt', do_not_check)
    # do_not_check = del_experts(do_not_check, 'Aktrcfylh Zqkj[fyjd')
    # write_experts('do_not_check.txt', do_not_check)
