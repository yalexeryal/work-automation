with open('nikname.txt', 'r') as nk:
    data = nk.read()

data = tuple(data.split("\n"))
rez =""
for i in data:
    rez = rez + i + ' '

print(f'/invite {rez}')
