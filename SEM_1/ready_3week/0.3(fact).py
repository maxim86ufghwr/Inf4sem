def fact(a,depth=0):
    if a==1:
        return 1
    print(depth)
    res = a * fact(a-1,depth+1)
    print(f'on step {depth}, fact = {res}')
    return res
b=int(input())
print(fact(b))