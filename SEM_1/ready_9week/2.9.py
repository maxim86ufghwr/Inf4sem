e = input()
u = ''
n = []
for i in e:
    if i in '0123456789':
        u += i
    elif i in '+-*/':
        n.append(i)

    else:
        n.append(u)
        u = ''
while '' in n:
    n.remove('')
print(n)
nu = 0
t = True
for i in n:
    if i[0] in '+-/*':
        if nu < 2:
            t = False
            print('Введено недостаточное количество оперантов')
        nu -= 1
    else:
        nu+=1
if nu != 1:
    print('Введено недостаточное количество операторов')
    t = False

while len(n) != 1 and t:
    op = []
    for i in range(len(n)):
        if n[i] in '+-*/':
            op.append(i)
    for i in op:
        if n[i-2][0] in '01234567890' and n[i-1][0] in '01234567890':
            t = n[i-2] + n[i] + n[i-1]
            print(t)
            y = str(eval(t))
            n.pop(i-2)
            n.pop(i-2)
            n[i-2] = y
print(n[0])

