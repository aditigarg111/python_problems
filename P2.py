# Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
values = input("enter values :").split(",")
list = list(values)  # or list = values.split(",")
Tuple = tuple(list)
print("list:",list)
print("Tuple:",Tuple)