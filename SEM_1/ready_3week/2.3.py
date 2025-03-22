import numpy as np
n = int(input())
common=[2,3]
t=[]
for i in range(4, n+1):
    er=True
    for j in range(2,int(np.sqrt(i))+1):
        if i%j==0:
            er=False
    if er:
        common.append(i)
print(common)
while n!=1:
    for i in common:
        if n % i == 0:
            t.append(i)
            n //= i
t.sort()
print(t)

