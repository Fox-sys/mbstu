while True:
    num = int(input())
    if ((num % 4 == 0) and not (num % 100 == 0)) or num % 400 == 0:
        print('yes')
    else:
        print('no')