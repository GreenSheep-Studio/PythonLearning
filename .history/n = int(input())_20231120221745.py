def YesIs(NumStr, n):
    Count = 0
    NumStr = NumStr + '0'
    i = 0
    while i < len(NumStr) - 2:
        if NumStr[i] == "1":
            for j in range(i, len(NumStr)):
                if NumStr[j] == "1":
                    Count += 1
                    if Count >= n and Count >= 3:
                        return "Yes"
                elif NumStr[j] == "0":
                    Count = 0
                    i = j + 1    
    return "No"

n, m = map(int, input().split())
ListTrue = []
for i in range(m):
    Num = input()
    ListTrue.append(YesIs(Num, n))
for x in ListTrue:
    print(x)