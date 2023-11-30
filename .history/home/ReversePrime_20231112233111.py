def main():
    count, i = 1, 2
    while count <= 10:
        if isPrime(i) and not isPalindrome(i) and isPrime(reverse(i)):
            print(i, end=" ")
            count += 1
        i += 1

def isPrime(number):
    divisor = 2
    while divisor <= number/2:
        if number % divisor == 0:
            return False
        divisor += 1
    return True

def isPalindrome(number):
    return number == reverse(number)

def reverse(number):
    result = 0
    while number != 0:
        remaiander = number % 10
        result = result * 10 + remaiander
        number = number // 10
    return result

if __name__ == "__main__":
    main()