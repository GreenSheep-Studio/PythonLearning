from rich.progress import track
from time import sleep
scoreList = list(input().split())
del(scoreList[-1])
Max = scoreList[0]
Min = scoreList[0]
for i in track(scoreList):
    if i > Max:
        Max = i
    elif i < Min:
        Min = i
    sleep(100)
Sum = 0
for i in scoreList:
    Sum += int(i)
Avg = (Sum - int(Max) - int(Min)) / (len(scoreList) - 2)
print(f"{Avg:.2f}")