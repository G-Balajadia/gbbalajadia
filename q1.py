#!/usr/bin/env python3

print("1. Convert inches -> cm")
print("2. Convert cm -> inches")

selection = input("Make your selection (1,2): ")


if int(selection) > 2:
    print('Invalid entry')
elif selection == '2':
    centimeters = input("Enter cm: ")
    inches = float(centimeters) / 2.54
    print('Number of inches: ' + str(inches))
else:
    inches = input("Enter inches: ")
    centimeters = float(inches)* 2.54
    print('Number of centimeters: ' + str(centimeters))


    