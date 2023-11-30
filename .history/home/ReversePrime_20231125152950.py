# 定义主函数
def main():
    # 初始化计数变量和i变量
    count, i = 1, 2
    # 当计数变量小于等于10时，执行循环
    while count <= 10:
        # 如果i是质数，不是回文数，并且反转后的i是质数，则打印i，并将计数变量加1
        if isPrime(i) and not isPalindrome(i) and isPrime(reverse(i)):
            print(i, end=" ")
            count += 1
        # 将i加1
        i += 1

# 定义判断质数函数
def isPrime(number):
    # 初始化除数变量
    divisor = 2
    # 当除数变量小于等于number的一半时，执行循环
    while divisor <= number/2:
        # 如果number能被除数变量整除，则返回False
        if number % divisor == 0:
            return False
        # 将除数变量加1
        divisor += 1
    # 否则返回True
    return True

# 定义判断回文数函数
def isPalindrome(number):
    # 如果number等于反转后的number，则返回True
    return number == reverse(number)

# 定义反转函数
def reverse(number):
    # 初始化结果变量
    result = 0
    # 当number不等于0时，执行循环
    while number != 0:
        # 获取number的余数
        remaiander = number % 10
        # 将余数乘以10，再加上结果变量，并将结果变量乘以10，再加上余数
        result = result * 10 + remaiander
        number = number // 10
    # 返回结果变量
    return result

# 如果当前文件是主函数，则执行main函数
if __name__ == "__main__":
    main()