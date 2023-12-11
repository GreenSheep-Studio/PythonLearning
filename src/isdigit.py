n = input("Enter a number: ")
if n.isdigit():
    if int(n) > 0:
        print('Positivo')
    else:
        print('err')
else:
    print('err')
