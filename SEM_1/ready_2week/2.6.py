a=list(map(int,input().split()))
for i in range(len(a)-1):
    t=True
    y=0
    for j in range(len(a)):
        if a[i]==a[j]:
            y+=1
    if y<=1:
        print(a[i],end=' ')
