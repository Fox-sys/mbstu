l1 = [i for i in range(1, 101)]
l2 = l1.copy()
l3 = l1

print(l3 is l1)
print(l2 is l1)

for i in l1:
    print(i)