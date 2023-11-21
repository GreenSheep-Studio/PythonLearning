ListNum = [x for x in input().split(",")]
accumulation = 1
for i in ListNum:
    accumulation *= int(i)
print(accumulation)