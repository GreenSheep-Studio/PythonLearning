def YesIs(NumStr, n):
    Count = 0
    list(NumStr).append("0")
    for i in range(len(NumStr)):
        if NumStr[i] == "1":
            for j in range(i, len(NumStr)):
                if NumStr[j] == "1":
                    Count += 1
                    if Count >= n:
                        return "Yes"
                elif NumStr[j] == "0":
                    Count = 0
                    continue    
    return "No"

n, m = map(int, input().split())
ListTrue = []
for i in range(m):
    Num = input()
    ListTrue.append(YesIs(Num, n))
for x in ListTrue:
    print(x)