#该函数用于求解n！的值
def Fact(n):
  '''
  计算正整数n的阶乘 n！
  '''
  if n == 0:
    return 1
  else:
    return n * Fact(n-1)                                       #利用递归实现阶乘的计算

#该函数是该程序的核心实现函数，用于实现阶乘序列求和
def FactSum1(n):
  '''
  阶乘求和，输入正整数n，输出1！+2！+3！+...+n!

  输入的为正整数，若非正整数输出 err
  '''
  if n.isdigit():                                              #判断输入的是否为一个数字 
    if int(n) > 0:                                             #判断输入的是否为正整数
      Sum = 0
      for i in range(1, int(n)+ 1):
        Sum += Fact(i)                                         #循环遍历，计算阶乘
    else:
      return "err"                                             #对不符合要求的输入进行错误处理
    Sum = "{:,}".format(Sum)                                   #设置Sum的格式为千分位
    return Sum                                                 #返回Sum
  else:
    return "err"                                               #对不符合要求的输入进行错误处理

def FactSum2(n):
  List = []
  List.append(1)
  if n.isdigit():
    if int(n) > 0:
      for i in range(1,int(n) + 1):
        List.append(i * List[i - 1])
      Sum = sum(List) - 1
    else:
      return "err"
    Sum = "{:,}".format(Sum)
    return Sum
  else:
    return "err"
        
#此为测试函数入口，用于测试核心函数FactSum1()的正确性
def testFactSum():
  '''
  测试 FactSum()函数

  已通过全部测设数据
  '''
  #
  assert FactSum1("9") == "409,113"                             #正整数9，输出409，113
  assert FactSum1("0") == "err"                                 #非正整数0,输出err
  assert FactSum1("-1") == "err"                                #负整数-1,输出err
  assert FactSum1("a") == "err"                                 #非数字a,输出err
  assert FactSum1("1.5") == "err"                               #小数1.5，输出err

  #
  assert FactSum2("9") == "409,113"                             #正整数9，输出409，113
  assert FactSum2("0") == "err"                                 #非正整数0,输出err
  assert FactSum2("-1") == "err"                                #负整数-1,输出err
  assert FactSum2("a") == "err"                                 #非数字a,输出err
  assert FactSum2("1.5") == "err"                               #小数1.5，输出err

#主函数，调用测试函数和核心函数FactSum1()，为程序运行主体
def main():
  print(testFactSum.__doc__)
  testFactSum()                                                #调用测试函数
  print(FactSum1.__doc__)
  while 1:
    n = input()                                                #输入n
    if n:                                                      #输入不为空
      print(f"调用FactSum1,输出为{FactSum1(n)}")                 #调用核心函数FactSum1()
      print(f"调用FactSum2,输出为{FactSum2(n)}")
    else:
      break                                                    #输入为空，退出循环

#调用main()函数
print(__name__)
if __name__ == '__main__':
  main()                                                       #调用main()函数