# This program checks if the input is a string or a number
a = input("Please enter a number: ")

# Checks if it is a string
if a.isalpha():
    print("It's a string")

# Checks if it is a positive number
elif a.isdigit():
    print("The number", a, "is a positive number.")

# Checks if it is a negative number
elif int(a) < 0:
    print("The number", a, "is a negative number.")