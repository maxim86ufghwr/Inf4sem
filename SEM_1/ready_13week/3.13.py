import random
def sort_Toni(n):
    if len(n) > 1:
        num = random.choice(n)
        eq = []
        more = []
        less = []
        for i in n:
            if i > num:
                more.append(i)
            elif i == num:
                eq.append(i)
            else:
                less.append(i)
        return sort_Toni(less) + eq + sort_Toni(more)
    else:
        return n
n = list(map(float, input().split()))

def test(m):
    h = True
    for i in m:
        assert isinstance(i, (int, float))
    assert h, "letter in list"
    p = True
    m = sort_Toni(m)
    for i in range(len(m)-1):
        if m[i] >= m[i+1]:
            p = False
    assert p, "bad sort"

test(n)
print(sort_Toni(n))
