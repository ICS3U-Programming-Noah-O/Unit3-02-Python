#!/usr/bin/env python3
# Created By: Noah Ouellette
# Date: Dec. 8, 2021
# This program allows a user to guess a number between 0 and 9

import constants
import colorama
import time
from colorama import Fore, Back, Style


def main():
    # This function asks for the users number and
    # then compares it to the constant

    # Input
    print(Fore.WHITE + "I have picked a number between 0 and 9.")
    time.sleep(1)
    print(Fore.WHITE + "Guess my number!!!")
    print(Fore.BLUE + " ")
    user_num = int(input("Enter your guess: "))

    # Process/Output
    time.sleep(1)
    print(Fore.CYAN + " ")
    if user_num == constants.RANDOM_NUM:
        print("You guessed it! Most impressive.")
    else:
        print("Sorry, that is incorrect. Try again")
        print("")
        time.sleep(1)
        main()


if __name__ == "__main__":
    main()
