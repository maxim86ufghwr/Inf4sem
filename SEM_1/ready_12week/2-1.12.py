line = ''
while line[-4:] != 'stop':
    line += input()
count = dict()
line = line.replace(' ', '')
line = line.replace('.', '')
line = line.replace('?', '')
line = line.replace(':', '')
line = line.replace(';', '')
line = line.replace('(', '')
line = line.replace(')', '')
f = len(line)-4
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
for i in alphabet:
    count[i.lower()] = 0
for i in line:
    if i in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя":
        count[i.lower()] += 1
for i in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя":
    print(i, round(count[i] / f * 100, 3))
# stop, чтобы остановить