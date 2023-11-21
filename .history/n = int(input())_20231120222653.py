def YesIs(NumStr, n):
    Count = 0
    NumStr = NumStr + '0'
    for i in range(len(NumStr)):
        if NumStr[i] == "1":
            Count += 1
            if Count >= n and Count >= 3:
                return "Yes"
        else:
            Count = 0
    return "No"

n, m = map(int, input().split())
ListTrue = []
for i in range(m):
    Num = input()
    ListTrue.append(YesIs(Num, n))
for x in ListTrue:
    print(x)
