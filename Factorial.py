userNumber = input("What number do you want the factorial of? ")
n = int(userNumber)
i = n
while i > 1:
    n = n * (i - 1)
    i = i - 1
print( "The factorial of", userNumber, "is", n )