def main():
    k = eval(input())
    List = []
    List.append(0)
    List.append(2)
    List.append(List[1] + List[1] + 1)
    if k == 1:
        print(2)
    elif k == 2:
        print(5)
    elif k > 2:
        for i in range (3, k + 1):
            List.append(List[2] * 2 + List[1])
            List.pop(0)
        print(List[2] % 998244353)

if __name__ == '__main__':
  main() 
        