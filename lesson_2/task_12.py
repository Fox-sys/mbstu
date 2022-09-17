def is_divisible_by_6(x: int):
    sum_of_nums = sum(map(int, [i for i in str(x)]))
    return (int(str(x)[-1]) % 2 == 0) and (sum_of_nums % 3 == 0)
