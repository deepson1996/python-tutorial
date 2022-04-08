'''
   List comprehension:  Elegent way to create list based on existing list
   Very kaam aauchha
   yo dictionary as well as set ko laagi use hunchha
'''
 # Traditional way
a = [3, 6, 7, 8, 9, 2, 4, 23, 75, 23, 123, 67]
b = []
for item in a:
    if item%2 == 0:
        b.append(item)

print(b)

# List comprehension way:

b = [i for i in a if i%2==0] # for i in a if i is even than push i
print(b)