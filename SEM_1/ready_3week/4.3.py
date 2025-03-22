n, word=map(str, input().split())
n=int(n)
if n%2==0:
    odd=0
else:
    odd=1
for i in range(n//2+odd):
    print(word*(i+1))
for i in range(n//2,0,-1):
    print(word * i)