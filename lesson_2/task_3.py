nums = list(map(int, input().split()))

uniq_nums = set(nums)
diff = len(nums) - len(uniq_nums)
if diff == 0:
    print(diff)
else:
    print(diff+1)