drink = int(input("Hello, what would you like to drink?\nPlease enter 1 to see our wine selection.\nPlease press 2 to see our non-alcoholic drink selection.\n"))
#1 chooses wine | 2 chooses soft drinks
if drink == 1:
    age = input("Are you 21 or over?")
    if age == "yes":
        print("Please let me check your ID so I can return with your choice of wine")
    else:
        print("I'm terribly sorry, but according to federal law it is illegal to serve alcohol to minors. Please choose a soft drink.")
else:
    print("I will return with your soft drink")