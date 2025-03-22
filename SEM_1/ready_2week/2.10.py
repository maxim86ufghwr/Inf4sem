with open('input2.txt', 'r', encoding='utf-8') as f:
    a = f.readlines()
print(a)
b=''
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] in 'уеэоаыяиюУЕЭОАЫЯИЮ':
            b+=a[i][j]+'с'+a[i][j]
        else:
            b+=a[i][j]
print(b)