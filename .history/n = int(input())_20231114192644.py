n, m = input().split()
n = int(n)
m = int(m)
while True:
    NumStr = input()
    if NumStr:
        Count = 0
        for i in range(len(NumStr)):
            if NumStr[i] == "1":
                if i < len(NumStr) - 1:
                    if NumStr[i + 1] == "1":
                        Count += 1
                        if Count >= n:
                            print("Yes")
                            continue
                    else:
                        Count = 0
                        print("No")
                        continue
                else:
                    print("No")
                    continue
    elif NumStr != True:
        break          
