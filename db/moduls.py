training_blocks = [
    ['JAVA', 'JM'],
    ['BHJ', 'SHFEBHJ'],
    ['IQA', 'QAPTL'],
    ['BTRX', 'INFO-BTRX', 'BWEB', 'BPATTI', 'BPATTC', 'BCONT', 'BBAY', 'FBTRX'],
    ['CPP', 'INFO-CPP', 'CPPS', 'CPPM', 'ALGOCPP', 'CPPL', 'SQLCPP', 'MAP', 'DPCPP', 'QT', 'IOT', 'PUE', 'FCPP'],
    ['DEVOPS', 'INFO-DEVOPS', 'MNT', 'DEVKUB', 'CLOKUB', 'GIT-DEV', 'VIRTD', 'TER', 'KONF', 'CICD-DEV', 'MON-DEV',
     'MICROS', 'KUBER', 'CLOPRO', 'BD-DEV', 'FDEVOPS', 'INFO-SHDEVOPS', 'SHVIRDTD', 'SHTER', 'SHKONF', 'SHCICD-DEV',
     'SHMON-DEV', 'SHMICROS', 'SHKUBER', 'SHCLOPRO', 'SHVIRTD'],
    ['PY', 'PYAPI', 'SQLPY', 'PDPTL', 'PDPTS'],
    ['FPY', 'FPYMQ', 'FPYJS', 'FPYAJS', 'FPYAHJ', 'FFPY'],
    ['IOS', 'info-ios', 'BIOS', 'IBALGO', 'AIOS', 'IOSUI', 'IOSINT', 'IOSDT', 'IOSADV', 'FIOS'],
    ['NDJS', 'INFO-NDJS', 'NDSE', 'NDTNF', 'FNDJS'],
    ['NTW', 'INFO-NTW', 'BNTW', 'RUTSW', 'RSNT', 'DRUT', 'SECNT', 'WFNT', 'QOS', 'CRPNT', 'OPTNT', 'IPNT', 'FNTW'],
    ['ONEC', 'INFO-ONEC', 'INFO-ONECMID', 'SRK', 'BALGO', 'VY', 'INF', 'SID', 'REGIS', 'FILE', 'RNFD', 'IND', 'MA',
     'PV', 'BPZ', 'DTK', 'BSP', 'OCEDT', 'TAT', 'MROC', 'OCPS', 'FONEC', 'FONECMID'],
    ['PAE', 'PBAS', 'PWIN', 'PNET', 'SCADA', 'PHD', 'CODEPLC', 'PIB', 'PMS', 'FPAE', 'INFO-PAE'],
    ['QAMID', 'FAQA', 'JSQA', 'JSAQA', 'MQA', 'LOADQA', 'IBQA', 'SMQA'],
    ['SHQA', 'INFO-SHQA', 'SQLSHQA', 'SMQA', 'FSHQA'],
    ['SIB', 'INFOSIB', 'IBB', 'IBNET', 'IBGIT', 'IBOS', 'IBDEV', 'IBWEB', 'IBDEF', 'IBMOD', 'IBINC', 'FIB', 'IBDEFOS',
     'IBSZI', 'IBNETK', 'FSHIB'],
    ['SQLD', 'SQLQA', 'SQLSLIN', 'SQLBASH', 'DWH-SQLD', 'SQLSDB', 'SQLDB', 'SQLAR', 'INFO-SIB'],
    ['SYS', 'SRLB', 'SDB', 'SLINA', 'SLINB', 'SLINC', 'NET', 'BASH', 'SVIRT', 'CICD', 'SMON', 'SFLT', 'SYSDB', 'SDBSQL',
     'SYSSEC', 'SLINA-LINUX', 'NET-LINUX', 'COURSE-FOPS', 'GIT-FOPS', 'FSYS', 'INFO-FOPS', 'INFO-SYS']
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

def reade_db_file(file):
    with open(file, 'r', encoding='UTF-8') as nc:
        db_file = nc.read()
        result = set(db_file.split('\n'))
        return result


def update_experts(file):
    experts = reade_db_file(file)
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
    do_not_check = reade_db_file('do_not_check.db')
    soft_experts = reade_db_file('soft_experts.db')
    print(update_experts(soft_experts))
    # do_not_check = update_experts(do_not_check, 'Aktrcfylh Zqkj[fyjd')
    # write_experts('do_not_check.txt', do_not_check)
    # do_not_check = del_experts(do_not_check, 'Aktrcfylh Zqkj[fyjd')
    # write_experts('do_not_check.txt', do_not_check)
