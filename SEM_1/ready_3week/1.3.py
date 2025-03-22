def fib(a, fibs):
    if a == 1:
        fibs[0] = 0
        return 0
    elif a == 2:
        fibs[1] = 1
        return 1
    elif fibs[a-1] !=0:
        return fibs[a-1]
    fibs[a-1] = fib(a-1, fibs) + fib(a-2, fibs)
    print(fibs)
    return fibs[a-1]
s = int(input())
fibs = [0 for i in range(s)]
print(fib(s, fibs))