def main():
    k = eval(input())
    List = []
    List[1] = 2
    List[2] = List[1] + List[1] + 1
    for i in range (3, k + 1):
        List[i] = List[i - 1] + List[1] + List[i - 2] +List[2]
    
    print(List[k + 1] % 998244353)
        