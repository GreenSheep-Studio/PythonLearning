n, m = input().split()
n = int(n)
m = int(m)
while True:
    NumStr = input()
    if NumStr:
        Count = 0
        for i in NumStr:
            if i  == '1':
                Count += 1
                if Count >= n:
                    print('Yes')
                    continue
            else:
                Count = 0
                print('No')
