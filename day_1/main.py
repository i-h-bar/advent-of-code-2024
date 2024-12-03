list_1 = [3, 4, 2, 1, 3, 3]
list_2 = [4, 3, 5, 3, 9, 3]

total = sum((abs(a - b) for a, b in zip(sorted(list_1), sorted(list_2))))
print(total)
