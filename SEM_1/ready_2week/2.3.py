st=input()
L = len(st)//2
pal=True
mir=True
for i in range(L):
    if st[i]!=st[-i-1]:
        pal=False
    if not(((st[i]==st[-i-1]) and (st[i] in 'AHIMOTUVWXY18')) or (st[i]=='3' and st[-i-1]=='E') or
    (st[i]=='E' and st[-i-1]=='3') or (st[i]=='L' and st[-i-1]=='J') or (st[i]=='J' and st[-i-1]=='L') or (st[i]=='S' and st[-i-1]=='2') or
    (st[i]=='2' and st[-i-1]=='S') or (st[i]=='Z' and st[-i-1]=='5') or (st[i]=='5' and st[-i-1]=='Z')):
        mir=False

res = f'''{st} palindrom = {pal}
{st} mirror string = {mir}'''
print(res)