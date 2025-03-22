import string as st
di = {}
all = []
f = open('javahelp_license.txt')
for l in f:
    l = l.lower()
    for i in range(len(l)):
        if l[i] in st.punctuation or l[i] in '1234567890':
            l = l.replace(l[i], ' ', 1)
    e = list(l.split())
    if len(e) > 0:
        all.append(e)
print(all)
f.close()
for i in range(len(all)):
    for j in range(len(all[i])):
        if not(all[i][j] in di.keys()):
            di[all[i][j]] = 1
        else:
            di[all[i][j]] += 1
max = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0, '10':0}
ma=['','','','','','','','','','']
a = list(di.keys())
b = list(di.values())
for i in range(len(b)):
    for j in range(len(max.values())):
        if int(b[i]) > max[str(j+1)]:
            max[str(j + 1)] = b[j]
            ma[j]=a[i]
            break
print(max,ma,sep='\n')



