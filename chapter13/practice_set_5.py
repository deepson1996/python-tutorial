from functools import reduce
l = [1, 2, 3, 4, 5, 6, 10, 12, 20, 15]

val = reduce(max, l)
print(val)