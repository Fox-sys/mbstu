nums = list(map(int, input('Введите ряд чисел через пробел: ').split(' ')))
min_num, max_num = int(input('Введите низ диапозона: ')), int(input('Введите верх диапозона: '))

if max_num < min_num:
    raise Exception(f'Диапозон указан не верно, максимальное число ({max_num}) < минимальное ({min_num})')

min_result = max_num + 1
for num in nums:
    while num > max_num or num < min_num:
        num = int(input(f'Введите число входящее черз диопазон, сейчас допустимы числа между {min_num} и {max_num}: '))
    if min_result >= num:
        min_result = num

print(f'Минимальное число в диапозоне: {min_result}')
