import numpy as np
def mult(n):
    common = [2, 3]
    t = []
    for i in range(4, n+1):
        er = True
        for j in range(2, int(np.sqrt(i))+1):
            if i % j == 0:
                er = False
        if er:
            common.append(i)
    while n != 1:
        for i in common:
            if n % i == 0:
                t.append(i)
                n //= i
    return t
def test_multiple(a):
    mu = mult(a)
    multi = 1
    for i in mu:
        multi *= i
    assert multi == a, "simple multiple isn't right"

f = int(input())
j = mult(f)
test_multiple(f)
print(j)


