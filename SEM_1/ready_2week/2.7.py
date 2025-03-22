a=list(map(int,input().split()))
b=set() # - это не список, строка или срез, а множество
for i in a:
    b.add(i)
ma=0
h=0
for i in b:
    if a.count(i) > ma:
        ma=a.count(i)
        h=i
print(h)