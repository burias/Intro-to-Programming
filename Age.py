x = input("What is your age?")
def Age(x):
    try:
        if int(x) >= 20:
            print("You're old")
        elif int(x) < 20:
            print("You're young")
        else:
            print("Please type a number")
    except ValueError:
        print("Please enter an integer")
Age(x)