#!/usr/bin/env python3
# Created By: Sam V
# Date: Nov 11, 2026
# This program calculates the squares of whole numbers from 0 to a user-defined limit (0 or greater).

# Prompt the user for a whole number

# Variable to control the validation loop
validInput = False

# Keep asking until the user enters a valid whole number
while not validInput:
    userInput = input("Enter a whole number: ")

    try:
        # Convert the text input into an integer
        limit = int(userInput)

        # Check if the number is negative
        if limit < 0:
            print("Invalid entry. Please enter a whole number (0 or greater).")
        else:
            # Input is valid, exit the while loop
            validInput = True

    except ValueError:
        # Catch errors if the user enters letters, symbols, or decimals
        print("Invalid entry. You must enter a valid whole number.")

# Loop from 0 up to and including the limit
for i in range(limit + 1):
    square = i * i
    print(str(i) + "^2 = " + str(square))
