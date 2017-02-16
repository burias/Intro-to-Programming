gasTank = int(input("""Hello user, in order for me to calculate the efficiency for the car you specify, I will need some data.
\nHow many gallons of gas are currently in the tank? """))
fuelEffic = int(input("How many miles per one gallon of gasoline does your car get? "))
gasPrice = int(input("You must have passed some gas stations on the way here, what is the price right now? "))

print ("Well, according to the data that you gave me, the cost in gas for driving 100 miles should be $%.2f" % (100/fuelEffic)*gasPrice)
print ("Wow! That means that with the", gasTank, "gallons in your tank you can go", gasTank*fuelEffic, "miles!")