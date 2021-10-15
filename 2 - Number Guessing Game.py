# I am using a library called "random"
# to help me generate a random number
import random

# This function checks if the user is correct
def checkNumber(randomInteger, userInput):
    while(randomInteger != userInput):

    # As long as the user keeps getting the wrong answer

        # ========================= GIVE HINTS ===========================
        # Check if user answered too low
        if(userInput > randomInteger):
            print("\nThe value is less than your answer.")

        # Check if user answered too high
        else:
            print("\nThe value is greater than your answer.")

        # Get input again
        userInput = int(input("What is the number: "))

    # If user got the right answer
    if (randomInteger == userInput):

        # User won the game
        print("\nYOU WON!"
              "\nThe correct number was " + str(randomInteger) + "!")


# This function gets executed first
def main():

    # Give directions to the user
    print("NUMBER GUESSING GAME\n")                 # Title of the game
    print("Guess the number from 1-10")

    randomInteger = random.randint(1,10)            # Saving my random number in a variable
    userInput = int(input("What is the number: "))  # Get user input

    checkNumber(randomInteger, userInput)           # Call the function


main()