with open('input.txt', 'r') as f:
    a = f.readlines()
b = ' '.join(a)
cou=0
for i in range(len(b)):
    if b[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        cou+=1
print(cou)