a = 12
b = 0

try:
    answer = a/b
    print(answer)
except ZeroDivisionError as err:
    print("Infinite")