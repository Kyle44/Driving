# File:        Driving.py
# Written by:  Kyle Fritz
# Date:        9/13/2013
# Lab Section: 10
# Description: This program calculates the total miles driven, the mileage in
#      miles per gallon, and the dollar cost per mile.

# def main() calculates the total miles driven by subtracting the initial
#      number of miles from the final number of miles. Then, it calculates
#      the mileage by dividing the total miles driven by the number of gallons
#      used. Finally, it calculates the cost per mile driven.


def main():
    print("This program calculates how many miles you drove, the MPG, and the cost per mile to operate your vehicle.")
    initial = eval(input("Enter your initial odometer reading: "))
    final = eval(input("Enter your final odometer reading: "))
    gallons = eval(input("Enter the number of gallons used: "))
    cost = eval(input("Enter the cost per gallon: "))
    tot = final - initial      # This is the total miles driven.
    mileage = tot / gallons    # This is the miles per gallon
    cost2 = cost / mileage     # This is the cost per mile.
    print("You drove", tot , "miles.")
    print("The mileage is" ,mileage, ".")
    print(round(cost2,2), "is the cost per mile.") # This rounds the cost per
    # mile to 2 decimal places.

main()
