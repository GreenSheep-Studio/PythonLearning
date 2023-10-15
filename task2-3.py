n,a = map(int,input().split())
aa = 0
sum = 0
for i in range(1,n+1):
    aa = aa*10+a
    sum += aa
print(sum)
