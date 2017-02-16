print("-" *50)
setOfColors = "black, white, yellow, blue, red"

color = input("Pick a color: ")
color = color.lower()

if setOfColors.find(color) >= 0:
    print("We have this color")
elif setOfColors.find(color) < 0:
    print("We do not have this color")
    
    