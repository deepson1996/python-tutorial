
try:
    a = int(input("Input enter a number: "))
    c = 1/a
except ValueError as ve:
    print(f"Value error {ve}")
except ZeroDivisionError as ze:
    print(f"Zero division error {ze}")
except Exception as e:
    print("Exception Occured")
print("Execution successful") #Executes by handling error exception nabhako bhaye yeta samma process nai pugthena