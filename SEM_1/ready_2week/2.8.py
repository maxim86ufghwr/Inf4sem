N = int(input())
a = list(map(int,input().split()))
for i in range(N):
    mor=0
    for j in range(N):
        if a[i]>a[j]:
            mor+=1
    if mor == N//2:
        print(a[i])