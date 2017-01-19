#This program calculates the given number of digits for the fibonacci sequence
fibo = [0 , 1];
digit = int(input("How many digits do you want? "))
i = 0
while i <= (digit - 3):
    a = fibo[-2]   
    b = fibo[-1]
    n = a + b 
    fibo.append(n)
    i += 1
print(fibo)