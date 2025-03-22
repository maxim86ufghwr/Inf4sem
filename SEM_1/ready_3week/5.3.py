N=int(input())
M=int(input())

B = []
for i in range(M):
    A = [0 for j in range(N)]
    B.append(A)
print(*B, sep='\n')
n1=N
m1=M
n0=0
m0=0
count=1
while n1>=n0 and m1>m0 and count<N*M:
    if count < N * M:
        for i in range(n0,n1):
            B[m0][i]=count
            count+=1
    if count < N * M:
        for i in range(m0+1,m1):
            B[i][n1-1] = count
            count += 1
    if count < N * M:
        for i in range(n1-2,n0-1,-1):
            B[m1-1][i] = count
            count += 1
    if count < N * M:
        for i in range(m1-2,m0,-1):
            B[i][n0] = count
            count += 1
    n0+=1
    m0+=1
    m1-=1
    n1-=1
for i in range(N):
    for j in range(M):
        if B[j][i]==0:
            B[j][i] = N*M
print(*B, sep='\n')