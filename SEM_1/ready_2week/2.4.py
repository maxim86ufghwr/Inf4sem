a = list(map(int,input().split()))
for i in range(0,len(a)//2):
    a[i*2],a[i*2+1] = a[i*2+1],a[i*2]
print(a)