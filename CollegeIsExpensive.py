# I assumed that the money is withdrawn before the interest rate is applied, 
# and the compound rate is applied to the account at the end of the month.
balance = 10000
rate = 0.005
months = 0

while balance >= 0:
    balance = balance - 500
    months = months + 1
    if balance <= 500:
        print ( "Thank you for banking with EvilCorp. \nUnfortunately, there are insufficient funds in the account to withdraw $500 \nAge of this account:" , months, "months." )
        break
    else:
        balance = balance * 1.005