n = int(input())
NumList = input().split(" ")
s = 0
List1 = []
for i in NumList:
    x = int(i)*s
    if x != 0:
        List1.append(x)
    s += 1
s = 0
List2 = []
for i in List1:
    x = int(i)*s
    if x != 0:
        List2.append(x)
    s += 1
for i in List2:
    print(i, end=" ")