#5-1
def isPass(score, n = 60):
    if score >= n:
        return "passe"
    else:
        return "failed"
stuA = 80
print(isPass(stuA))
stuB = 120
print(isPass(stuB, 90))

#5-2
def fun(m,n):
    ls = []
    for i in range(m,n+1):
        if i < 2:
            continue
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            ls.append(i)
    return ls
m, n = map(int, input().split())
print(sum(fun(m,n)))
