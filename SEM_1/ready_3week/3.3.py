a,b=map(int,input().split())
a1=a
b1=b
d=0
while a1!=0 and b1!=0:
    if a1>b1:
        a1=a1%b1
    else:
        b1=b1%a1
    d=a1+b1
is_find=True
for x in range(a):
    for y in range(b):
        if (-1*(a*x) + (b*y)) == d and is_find:
            print(-x, y, d)
            is_find = False
        elif (a*x) - (b*y) == d and is_find:
            print(x,-y, d)
            is_find = False