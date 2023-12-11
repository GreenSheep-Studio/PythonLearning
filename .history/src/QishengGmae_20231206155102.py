def main():
    k = eval(input())
    List = []
    List.append(0)
    List.append(2)
    List.append(List[1] + List[1] + 1)
    if k == 1:
        print(1)
    elif k == 2:
        print(5)
    elif k > 2:
        for i in range (3, k + 1):
            List.append(List[2] * 2 + List[1])
        print(List[3] % 998244353)

if __name__ == '__main__':
  main() 
        