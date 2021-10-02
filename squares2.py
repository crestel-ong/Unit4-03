#!/usr/bin/env python3

# Created by: Crestel Ong
# Created on: Sept 2021
# This is squares program in python


def main():
    # this function squares the numbers from 0 to whatever...
    # number before the number you entered

    # declaring
    counter = 0
    squared = 0

    # input
    user_input_as_string = input("Enter an integer >= 0: ")

    try:
        # convert string to integer
        user_input_as_integer = int(user_input_as_string)

        # process and output
        if user_input_as_integer > 0:
            for counter in range(user_input_as_integer + 1):
                squared = counter ** 2
                print("{0}² = {1}.".format(counter, squared))
        else:
            print("You did not enter a positive integer.")
    except Exception:
        print("You did not enter an integer.")

    print("\nDone.")


if __name__ == "__main__":
    main()
