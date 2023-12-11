def main():
    k = eval(input())
    List = []
    List.append(0)
    List.append(2)
    List.append(List[1] + List[1] + 1)
    for i in range (3, k + 1):
        List.append(List[i - 1] + List[1] + List[i - 2] +List[2])
    
    print(List[k] % 998244353)

if __name__ == '__main__':
  main() 
        