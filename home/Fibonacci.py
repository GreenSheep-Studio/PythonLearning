def fib(n):
    fiblist = []
    if n == 0:
        fiblist.append(0)
    elif n == 1:
        fiblist.append(1)
    else:
        fiblist.append(1)
        fiblist.append(1)
        while fiblist[-1] + fiblist[-2] <= n:
            fiblist.append(fiblist[-1] + fiblist[-2])
    return fiblist

n = int(input())
fiblist = fib(n)
print(fiblist)