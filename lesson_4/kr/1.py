s = 0
while (a := int(input())) != 0:
    if a % 2 == 0 or a <= 50:
        continue
    a += s

print(s)
