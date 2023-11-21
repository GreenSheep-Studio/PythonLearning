def fib(n):
    fiblist = []
    if n == 0:
        return fiblist
    elif n == 1:
        fiblist.append(0)
        return fiblist
    else:
        fiblist.append(0)
        fiblist.append(1)
        for i in range(2, n):
            fiblist.append(fiblist[i - 1] + fiblist[i - 2])
        return fiblist

n = int(input())
fiblist = fib(n)
print(fiblist)