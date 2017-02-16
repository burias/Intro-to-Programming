import random 
#random number from 1 to 10
a = random.randint(1,10)
#roulette
print("The goal is to get as close to 21 as possible without going over.")

i = 1
while i == 1 :
    if a > 21:
        print("You went over 21! You lost, try again.")
        if retry == "yes":
            i = 1
            a = random.randint(1,10)
        else:
            i = 0
            break
    else:
        while a < 22:
            print("Your number is now",a)
            if a == 21:
                print("You win! Congratulations.")
                retry = input("Would you like to try again? If so type \"yes\". ")
                if retry == "yes":
                    i = 1
                    a = random.randint(1,10)
                else:
                    i = 0
                    break
                break
            elif a < 21:
                retry = input("Would you like to keep going? If so type \"yes\". ")
                if retry == "yes":
                    i = 1
                    a += random.randint(1,10)
                else:
                    print("Your final number is", str(a) + ".")
                    i = 0
                    break
