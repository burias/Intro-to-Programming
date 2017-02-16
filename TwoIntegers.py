#This is some magic with integers
int1 = int(input("Hello! Please input an  integer. "))
int2 = int(input("Please enter a second integer. "))
intGroup = (int1, int2)
#The sum
intSum = int1 + int2

#The difference
intDif = int1 - int2

#The product
intPro = int1 * int2

#The average
intAvg = (int1 + int2) / 2

#The distance
intAbs = 0
if intDif < 0:
    intAbs = intDif * (-1)
else:
    intAbs = intDif

#The maximum
intMax = max(int1,int2)

#The minimum
intMin = min(int1, int2)

print("\n" + "-" * 50)
print("The sum of both integers is:", intSum)
print("\nThe difference of both numbers is:", intDif)
print("\nThe product of both integers is:", intSum)
print("\nThe average of both integers is:", intAvg)
print("\nThe distance of both integers is:", intAbs)
print("\nThe largest of both integers is:", intMax)
print("\nThe smallest of both integers is:", intMin)
print("" + "-" * 50)