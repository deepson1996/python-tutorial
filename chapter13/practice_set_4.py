l = [1, 2, 3, 4, 5, 6, 10, 12, 20, 15]

divisible = lambda l: l%5==0

new = list(filter(divisible, l))
print(new)