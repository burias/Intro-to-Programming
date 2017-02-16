startBalance = 10000
interestRate = 1.05
year = 0

if startBalance <= 20000:
    year += 1
    startBalance = ( startBalance * interestRate)
else:
    print( "You will reach 20,000 dollars in ", year, "years!")