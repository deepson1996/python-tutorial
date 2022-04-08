num = 20

table = [num*i for i in range(1, 11) if i%2==0]
print(table)
with open("tables.txt", "a") as f:
    f.write(str(table))
    f.write('\n')