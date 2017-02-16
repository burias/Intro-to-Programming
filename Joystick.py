#Get the direction from the joystick
joystick = int(input("Enter the position of the joystick (0-7)"))

#Joystick up
if joystick == 0:
    print("Moving up")

#Joystick diagonal up right
elif joystick == 1:
    print("Moving up and to the right")

#Joystick right
elif joystick == 2:
    print("Moving to the right")

#Joystick diagonal down right
elif joystick == 3:
    print("Moving down and to the right")

#Joystick diagonal down right
elif joystick == 4:
    print("Moving down")

#Joystick diagonal down right
elif joystick == 5:
    print("Moving down and to the left")

#Joystick diagonal down right
elif joystick == 6:
    print("Moving left")

#Joystick diagonal down right
elif joystick == 7:
    print("Moving up and to the left")
    
else:
    print("Joystick value out of range")
