# Code Listing #2

"""

Guessing game - version two with fix

"""

import random

# Some global password information which is hard-coded
passwords={"joe": "world123",
           "jane": "hello123"}

def game():
    """ A guessing game """

    # Use 'raw_input' to read standard input
    value = raw_input("Please enter your guess (between 1 and 10): ")

    try:
        value=int(value)
    except ValueError:
        print('Wrong type entered, try again',value)
        return
    
    print("Entered value is",value)
    if value == random.randrange(1, 10):
        print("You won!")
    else:
        print("Try again")

if __name__ == "__main__":
    game()
