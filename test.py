def Thousands(Num):
  NumOut = []
  '''
  实现千分位
  '''
  n = 0
  while 1:
    if Num < 1000:
      NumOut.append(Num)
      break
    else:
      NumOut.append(Num % 1000)
      NumOut.append(",")
      Num = Num // 1000
  NumOut = NumOut[::-1]
  for i in range(0, len(NumOut)):
    NumOut[i] = str(NumOut[i])
  return "".join(NumOut)

while 1:
  print(Thousands(int(input())))