#!/usr/bin/env python3

# created by: Trinity Armstrong
# created on: September 2019
# This program runs the "Number Guessing Game"


import constants


def main():
    # This function runs the "Number Guessing Game"

    # Input
    guess = int(input("Try and guess a number between 0 and 9 (integer): "))
    print("")

    # process
    if guess == constants.CORRECT_NUMBER:
        # Output 1
        print("You are correct!!! ")


if __name__ == "__main__":
    main()
