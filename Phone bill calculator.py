#Suppose your cell phone carrier charges you $29.95 for up to 300 minutes of
#calls, and $0.45 for each additional minute, plus 12.5 percent taxes and fees. Give
#an algorithm to compute the monthly charge from a given number of minutes.

# A fucntion to calculate the monthly price according to the amount of minutes
def bill ( minutes ) :
    basePrice = 29.95
    minuteRate = 0.45
    baseMinutes = 300
    if minutes >= baseMinutes :
        extraMinutes = minutes % baseMinutes
        extraPrice = ( extraMinutes * minuteRate )
        basePrice += extraPrice 
        return basePrice
    else:
        return basePrice
print ( "Your bill this month is $" , bill ( 300 ) )
print ( "Your bill this month is $" , bill ( 301 ) )
print ( "Your bill this month is $" , bill ( 400 ) )