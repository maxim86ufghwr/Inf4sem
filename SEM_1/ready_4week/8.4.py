import numpy as np
a = [np.random.randint(1, 100) for i in range(100)]
b = [np.random.randint(1, 100) for j in range(100)]
a_s = set(a[i] for i in range(100))
b_s = set(b[i] for i in range(100))
c = a+b
print(a,b,a_s,b_s,sep='\n')
print('Уникальные для a списка:',end=' ')
for i in a_s:
    if a.count(i) == 1:
        print(i, end=', ')
print()
print('Уникальные для b списка:',end=' ')
for i in b_s:
    if b.count(i) == 1:
        print(i, end=', ')
print()
print('Уникальные для объединения этих списков:',end=' ')
for i in a_s:
    if c.count(i) == 1:
        print(i, end=', ')
for i in b_s:
    if c.count(i) == 1:
        print(i, end=', ')
print()
print('Содержащиеся в обоих списках:',end=' ')
for i in a_s:
    if i in b_s:
        print(i, end=', ')
