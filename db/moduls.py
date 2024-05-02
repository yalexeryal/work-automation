training_blocks = [
    ['C-JAVA', 'JAVA', 'JM'],
    ['C-BHJ', 'BHJ', 'SHFEBHJ'],
    ['C-IQA', 'IQA', 'QAPTL'],
    ['BTRX', 'INFO-BTRX', 'BWEB', 'BPATTI', 'BPATTC', 'BCONT', 'BBAY', 'FBTRX'],
    ['CPP', 'INFO-CPP', 'CPPS', 'CPPM', 'ALGOCPP', 'CPPL', 'SQLCPP', 'MAP', 'DPCPP', 'QT', 'IOT', 'PUE', 'FCPP'],
    ['DEVOPS', 'INFO-DEVOPS', 'MNT', 'DEVKUB', 'CLOKUB', 'GIT-DEV', 'VIRTD', 'TER', 'KONF', 'CICD-DEV', 'MON-DEV',
     'MICROS', 'KUBER', 'CLOPRO', 'BD-DEV', 'FDEVOPS', 'INFO-SHDEVOPS', 'SHVIRDTD', 'SHTER', 'SHKONF', 'SHCICD-DEV',
     'SHMON-DEV', 'SHMICROS', 'SHKUBER', 'SHCLOPRO', 'SHVIRTD'],
    ['C-PY', 'PY', 'PYAPI', 'SQLPY', 'PDPTL', 'PDPTS'],
    ['C-FPY-ФРОНТЕНД', 'FPY', 'FPYMQ', 'FPYJS', 'FPYAJS', 'FPYAHJ', 'FFPY'],
    ['IOS', 'info-ios', 'BIOS', 'IBALGO', 'AIOS', 'IOSUI', 'IOSINT', 'IOSDT', 'IOSADV', 'FIOS'],
    ['NDJS', 'INFO-NDJS', 'NDSE', 'NDTNF', 'FNDJS'],
    ['NTW', 'INFO-NTW', 'BNTW', 'RUTSW', 'RSNT', 'DRUT', 'SECNT', 'WFNT', 'QOS', 'CRPNT', 'OPTNT', 'IPNT', 'FNTW'],
    ['ONEC-ONECMID', 'ONEC', 'INFO-ONEC', 'INFO-ONECMID', 'SRK', 'BALGO', 'VY', 'INF', 'SID', 'REGIS', 'FILE', 'RNFD', 'IND', 'MA',
     'PV', 'BPZ', 'DTK', 'BSP', 'OCEDT', 'TAT', 'MROC', 'OCPS', 'FONEC', 'FONECMID'],
    ['PAE', 'PBAS', 'PWIN', 'PNET', 'SCADA', 'PHD', 'CODEPLC', 'PIB', 'PMS', 'FPAE', 'PSQL', 'INFO-PAE'],
    ['QAMID', 'FAQA', 'JSQA', 'JSAQA', 'MQA', 'LOADQA', 'IBQA', 'SMQA'],
    ['SHQA', 'INFO-SHQA', 'SQLSHQA', 'SMQA', 'FSHQA'],
    ['SIB', 'INFOSIB', 'IBB', 'IBNET', 'IBGIT', 'IBOS', 'IBDEV', 'IBWEB', 'IBDEF', 'IBMOD', 'IBINC', 'FIB', 'IBDEFOS',
     'IBSZI', 'IBNETK', 'FSHIB'],
    ['SQLD', 'SQLQA', 'SQLSLIN', 'SQLBASH', 'DWH-SQLD', 'SQLSDB', 'SQLDB', 'SQLAR', 'INFO-SIB'],
    ['SYS', 'SRLB', 'SDB', 'SLINA', 'SLINB', 'SLINC', 'NET', 'BASH', 'SVIRT', 'CICD', 'SMON', 'SFLT', 'SYSDB', 'SDBSQL',
     'SYSSEC', 'SLINA-LINUX', 'NET-LINUX', 'COURSE-FOPS', 'GIT-FOPS', 'FSYS', 'INFO-FOPS', 'INFO-SYS'],
    ['ANALITIKA', 'ABT', 'APID', 'ATR', 'BIC', 'CVML', 'DSNN', 'DST', 'FEML', 'HRP', 'HRPAL', 'MLOP', 'PBI', 'PDX',
     'RNFDA', 'RNFDAP', 'RSML', 'TSML', 'XLS', 'DSQ', 'MCA', 'YZDA', 'DIPLOM-DSU', 'DLL', 'PDC', 'PGS', 'BANZ', 'ATRA',
     'DSW', 'HRONB', 'INFO-OCA', 'INFO-HRM', 'MAA', 'MBPA', 'NUMPY', 'PWH', 'PYDA', 'SSOCA', 'STPY', 'TL', 'WSDL', 'MBP',
     'DIPLOM-DJO', 'DSML', 'GPT-3', 'MDS', 'SQL', 'SQLP', 'ABP', 'ACV', 'DFD', 'IMBA', 'INFO-ABU', 'INFO-OCAMID', 'NLP',
     'PAF', 'SALFREE', 'TAB', 'UPK', 'FPS', 'GPT', 'INFO-ABI', 'INFO-DS', 'PYDA-DIPLOM', 'DAU', 'DVA', 'INFO-DMAR',
     'INFO-DSU', 'SDM', 'SDIT', 'ARCH-SAL', 'ROMAM'],
    ['C-PY-AD', 'ADPY'],
    ['C-AJS', 'AJS', 'SHFEJS'],
    ['C-DJ', 'DJSPD', 'DJ'],
    ['C-MQ', 'FDMQ', 'MQ']
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


if __name__ == "__mane__":
    do_not_check = reade_db_file('do_not_check.db')
    soft_experts = reade_db_file('soft_experts.db')
    print(update_experts(soft_experts))

